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
    """Browser-based SSO sequence (SAML Web Browser SSO / OIDC authorization code flow).

    The assertion or token travels through the user's browser (front channel); the SP
    validates it locally against the IdP's published keys and never sees the password.
    """
    fig, ax = plt.subplots(figsize=(14, 8.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9.4)
    ax.axis('off')

    xs = {'user': 2.0, 'sp': 7.0, 'idp': 12.0}
    top, bottom = 8.0, 0.9
    heads = [
        ('user', 'User / Browser', SURFACE_ALT, TEXT_LIGHT),
        ('sp', 'Service Provider\n(Application)', CYAN, TEXT_DARK),
        ('idp', 'Identity Provider\n(IdP)', PURPLE, TEXT_DARK),
    ]
    for key, label, color, tcolor in heads:
        rounded_box(ax, xs[key] - 1.3, top + 0.15, 2.6, 0.95, label, color, text_color=tcolor, fontsize=10)
        ax.plot([xs[key], xs[key]], [bottom, top + 0.1], color=SLATE, lw=1.2, ls=(0, (4, 4)), zorder=0)

    label_bbox = dict(boxstyle='round,pad=0.25', fc='white', ec='none')
    steps = [
        ('user', 'sp', 'left', '1. Request a protected resource', CYAN),
        ('sp', 'user', 'left', '2. Redirect to the IdP with a SAML AuthnRequest / OIDC authorization request', AMBER),
        ('user', 'idp', 'left', '3. Follow the redirect; user authenticates at the IdP (password + MFA)', EMERALD),
        ('idp', 'user', 'left', '4. IdP returns a signed SAML assertion / OIDC code or ID token via the browser', ROSE),
        ('user', 'sp', 'left', '5. Browser delivers the assertion, code, or token to the SP', ROSE),
    ]
    y = 7.35
    for src, dst, _, label, color in steps:
        arrow(ax, (xs[src], y), (xs[dst], y), color=color, lw=2.2)
        ax.text((xs[src] + xs[dst]) / 2, y + 0.2, label, ha='center', va='bottom', fontsize=10.5,
                color=DARK, bbox=label_bbox, zorder=3)
        y -= 1.0

    # Step 6: local validation at the SP (no call back to the IdP)
    rounded_box(ax, xs['sp'] - 2.3, y - 0.55, 4.6, 0.9,
                '6. SP validates signature, audience, and expiry', CYAN, text_color=TEXT_DARK, fontsize=10,
                subtext='SAML: IdP certificate from metadata  |  OIDC: IdP public keys (JWKS)')
    y -= 1.35
    arrow(ax, (xs['sp'], y), (xs['user'], y), color=CYAN, lw=2.2)
    ax.text((xs['sp'] + xs['user']) / 2, y + 0.2, '7. Session created; access granted', ha='center', va='bottom',
            fontsize=10.5, color=DARK, bbox=label_bbox, zorder=3)

    ax.text(7.0, 0.55, 'Next application: the browser is redirected to the IdP again, and the existing IdP session '
            'satisfies the request without a new prompt (SSO).', ha='center', fontsize=10, color=DARK)
    ax.text(7.0, 0.1, 'Trust rests on the IdP signature; the SP never sees the user\'s password. '
            '(OIDC code flow: the SP also redeems the code with the IdP directly.)',
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
        (5.7, 2.4, 2.2, 1.2, 'Compare to Template', EMERALD, 'Stored template'),
        (8.4, 2.4, 2.2, 1.2, 'Score vs. Threshold', AMBER, 'FAR / FRR tuning'),
        (11.1, 2.4, 2.6, 1.2, 'Accept or Reject', ROSE, 'Unlock the authenticator'),
    ]
    for x, y, w, h, text, color, sub in boxes:
        rounded_box(ax, x, y, w, h, text, color, text_color=TEXT_DARK, subtext=sub)

    for i in range(len(boxes) - 1):
        x_end = boxes[i][0] + boxes[i][2]
        x_next = boxes[i + 1][0]
        arrow(ax, (x_end, 3.0), (x_next, 3.0))

    ax.text(7.0, 1.4, 'False Accept Rate (FAR) and False Reject Rate (FRR) trade off at the decision threshold.',
            ha='center', fontsize=10.5, color=DARK)
    ax.text(7.0, 0.7, 'Templates are sensitive personal data — protect them, and prefer matching on the user\'s own device.',
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
