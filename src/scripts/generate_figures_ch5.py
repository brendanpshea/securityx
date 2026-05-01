import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

IMG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/assets/images'))
os.makedirs(IMG_DIR, exist_ok=True)

DARK = '#0f172a'
SURFACE = '#1e293b'
SURFACE_ALT = '#334155'
TEXT_DARK = '#0f172a'
TEXT_LIGHT = '#f8fafc'
CYAN = '#06b6d4'
PURPLE = '#a78bfa'
EMERALD = '#34d399'
AMBER = '#fbbf24'
ROSE = '#fb7185'
SLATE = '#64748b'


def rounded_box(ax, x, y, w, h, text, fc, ec='white', text_color=TEXT_LIGHT, fontsize=10, subtext=None):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle='round,pad=0.08,rounding_size=0.08',
        linewidth=1.8, edgecolor=ec, facecolor=fc
    )
    ax.add_patch(box)
    if subtext:
        ax.text(x + w / 2, y + h * 0.62, text, ha='center', va='center', color=text_color,
                fontsize=fontsize, fontweight='bold')
        ax.text(x + w / 2, y + h * 0.28, subtext, ha='center', va='center', color=text_color,
                fontsize=fontsize - 1)
    else:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', color=text_color,
                fontsize=fontsize, fontweight='bold')


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=ms, lw=lw, color=color))


def create_sso_workflow():
    fig, ax = plt.subplots(figsize=(14, 7.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    rounded_box(ax, 0.5, 6.3, 2.2, 1.0, 'User / Browser', SURFACE_ALT)
    rounded_box(ax, 5.7, 6.3, 2.6, 1.0, 'Service Provider\n(Application)', CYAN, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 11.0, 6.3, 2.6, 1.0, 'Identity Provider\n(IdP)', PURPLE, text_color=TEXT_DARK, fontsize=10)

    steps = [
        (0.5, 5.3, '1. Request app resource', (2.7, 6.8), (5.7, 6.8), CYAN),
        (0.5, 4.5, '2. Redirect to IdP with SAML / OIDC request', (5.7, 6.5), (2.7, 6.5), AMBER),
        (0.5, 3.7, '3. User authenticates (password + MFA)', (1.6, 6.3), (1.6, 5.0), EMERALD),
        (0.5, 2.9, '4. IdP redirects browser back with signed token / assertion', (11.0, 6.5), (8.3, 6.5), ROSE),
        (0.5, 2.1, '5. SP validates signature, issues session', (8.3, 6.8), (11.0, 6.8), CYAN),
        (0.5, 1.3, '6. Subsequent apps reuse the same IdP session (SSO)', None, None, SLATE),
    ]
    for sx, sy, label, *_ in steps:
        ax.text(sx, sy, label, fontsize=11, color=DARK, va='center')

    arrow(ax, (2.7, 6.85), (5.7, 6.85), color=CYAN)
    arrow(ax, (5.7, 6.55), (2.7, 6.55), color=AMBER)
    arrow(ax, (2.7, 6.4), (11.0, 6.4), color=PURPLE, lw=1.4, style='-')
    arrow(ax, (11.0, 6.7), (8.3, 6.7), color=ROSE)
    arrow(ax, (8.3, 7.0), (11.0, 7.0), color=EMERALD, lw=1.2, style='-')

    ax.text(7.0, 0.3, 'Trust is established by the IdP signature; the SP never sees the user password.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Federated Identity and SSO Workflow (SAML / OIDC)', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch05_sso_workflow.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_biometric_flow():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')

    boxes = [
        (0.3, 2.4, 2.2, 1.2, 'Capture', CYAN, 'Camera, sensor, mic'),
        (3.0, 2.4, 2.2, 1.2, 'Extract Features', PURPLE, 'Minutiae, vectors'),
        (5.7, 2.4, 2.2, 1.2, 'Compare to Template', EMERALD, 'Stored hash / vector'),
        (8.4, 2.4, 2.2, 1.2, 'Score vs. Threshold', AMBER, 'FAR / FRR tuning'),
        (11.1, 2.4, 2.6, 1.2, 'Accept or Reject', ROSE, 'Bind to identity'),
    ]
    for x, y, w, h, text, color, sub in boxes:
        rounded_box(ax, x, y, w, h, text, color, text_color=TEXT_DARK, subtext=sub)

    for i in range(len(boxes) - 1):
        x_end = boxes[i][0] + boxes[i][2]
        x_next = boxes[i + 1][0]
        arrow(ax, (x_end, 3.0), (x_next, 3.0))

    ax.text(7.0, 1.4, 'False Accept Rate (FAR) and False Reject Rate (FRR) trade off at the decision threshold.',
            ha='center', fontsize=10.5, color=DARK)
    ax.text(7.0, 0.7, 'Templates should be stored as one-way transformations — biometrics cannot be reissued if leaked.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Biometric Authentication Process Flow', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch05_biometric_flow.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 5 figures...')
    create_sso_workflow()
    create_biometric_flow()
    print('Chapter 5 figures generated successfully.')
