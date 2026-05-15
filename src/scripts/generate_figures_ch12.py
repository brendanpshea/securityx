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


def rounded_box(ax, x, y, w, h, text, fc, ec='white', text_color=TEXT_LIGHT,
                fontsize=10, subtext=None):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle='round,pad=0.08,rounding_size=0.08',
        linewidth=1.8, edgecolor=ec, facecolor=fc
    )
    ax.add_patch(box)
    if subtext:
        ax.text(x + w / 2, y + h * 0.65, text, ha='center', va='center',
                color=text_color, fontsize=fontsize, fontweight='bold')
        ax.text(x + w / 2, y + h * 0.30, subtext, ha='center', va='center',
                color=text_color, fontsize=fontsize - 1)
    else:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
                color=text_color, fontsize=fontsize, fontweight='bold')


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16, ls='-',
          connectionstyle=None):
    kwargs = {
        'arrowstyle': style,
        'mutation_scale': ms,
        'lw': lw,
        'color': color,
        'linestyle': ls,
    }
    if connectionstyle:
        kwargs['connectionstyle'] = connectionstyle
    ax.add_patch(FancyArrowPatch(start, end, **kwargs))


def create_soar_phishing_workflow():
    fig, ax = plt.subplots(figsize=(16, 8.8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.8)
    ax.axis('off')

    ax.text(1.8, 7.95, 'Detect', ha='center', va='bottom',
        fontsize=10, fontweight='bold', color=SLATE)
    ax.text(8.0, 7.95, 'Decide', ha='center', va='bottom',
        fontsize=10, fontweight='bold', color=SLATE)
    ax.text(12.8, 7.95, 'Respond', ha='center', va='bottom',
        fontsize=10, fontweight='bold', color=SLATE)

    rounded_box(ax, 0.5, 6.45, 2.5, 1.0,
        'Email Alert',
        SURFACE_ALT, fontsize=11,
        subtext='SEG flags suspicious message')
    rounded_box(ax, 3.6, 6.45, 3.0, 1.0,
        'Enrich + Score',
        CYAN, text_color=TEXT_DARK, fontsize=11,
        subtext='extract IOCs, query TIP and sandbox')

    diamond_cx, diamond_cy = 8.05, 6.95
    diamond_pts = [(diamond_cx, diamond_cy + 0.7),
           (diamond_cx + 1.15, diamond_cy),
           (diamond_cx, diamond_cy - 0.7),
           (diamond_cx - 1.15, diamond_cy)]
    diamond = plt.Polygon(diamond_pts, closed=True,
              facecolor=AMBER, edgecolor='white', linewidth=1.8)
    ax.add_patch(diamond)
    ax.text(diamond_cx, diamond_cy + 0.05, 'High', ha='center', va='center',
        color=TEXT_DARK, fontsize=10, fontweight='bold')
    ax.text(diamond_cx, diamond_cy - 0.18, 'confidence?', ha='center', va='center',
        color=TEXT_DARK, fontsize=10, fontweight='bold')

    rounded_box(ax, 6.8, 4.9, 2.4, 0.92,
        'Analyst Review',
        PURPLE, fontsize=10,
        subtext='low-confidence or ambiguous alerts')

    rounded_box(ax, 9.55, 6.45, 3.1, 1.0,
        'Quarantine + Block',
        ROSE, fontsize=11,
                subtext='remove mail, block URLs and IPs')
    rounded_box(ax, 13.1, 6.45, 2.7, 1.0,
        'Case + Notify',
        EMERALD, text_color=TEXT_DARK, fontsize=11,
                subtext='incident record and user guidance')
    rounded_box(ax, 9.55, 3.9, 3.1, 1.0,
        'Endpoint Follow-up',
        CYAN, text_color=TEXT_DARK, fontsize=11,
                subtext='EDR checks for click or execution')
    rounded_box(ax, 13.1, 3.9, 2.7, 1.0,
        'Isolate Endpoint',
        ROSE, fontsize=11,
                subtext='network isolate the compromised host')
    rounded_box(ax, 11.25, 1.35, 3.8, 1.0,
        'Post-Incident Review',
        SURFACE_ALT, fontsize=11,
        subtext='metrics, IOC export, and playbook tuning')

    arrow(ax, (3.0, 6.95), (3.6, 6.95), color=SLATE, lw=1.8)
    arrow(ax, (6.6, 6.95), (6.95, 6.95), color=CYAN, lw=1.8)
    arrow(ax, (8.05, 7.65), (8.05, 5.82), color=PURPLE, lw=1.8)
    arrow(ax, (9.2, 6.95), (9.55, 6.95), color=AMBER, lw=1.8)
    arrow(ax, (12.65, 6.95), (13.1, 6.95), color=ROSE, lw=1.8)
    arrow(ax, (11.1, 6.45), (11.1, 4.9), color=ROSE, lw=1.8)
    arrow(ax, (14.45, 6.45), (14.45, 2.35), color=EMERALD, lw=1.6, ls='--')
    arrow(ax, (12.65, 4.4), (13.1, 4.4), color=CYAN, lw=1.8)
    arrow(ax, (11.1, 3.9), (12.2, 2.35), color=SLATE, lw=1.6, ls='--')
    arrow(ax, (14.45, 3.9), (13.55, 2.35), color=ROSE, lw=1.8)

    ax.text(8.45, 7.18, 'Yes', color=TEXT_DARK, fontsize=8.5, fontweight='bold')
    ax.text(8.25, 5.95, 'No', color=PURPLE, fontsize=8.5, fontweight='bold')
    ax.text(12.95, 2.55, 'no host impact', color=SLATE, fontsize=8, style='italic')
    ax.text(14.75, 2.7, 'host interacted', color=ROSE, fontsize=8, style='italic', rotation=90)

    ax.text(8.0, 0.35,
        'Low-confidence alerts branch to analyst review. Endpoint isolation happens only when telemetry shows user interaction.',
        ha='center', fontsize=9, color=SLATE, style='italic')

    plt.title('Automated SOAR Phishing Response Workflow',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch12_soar_phishing.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_nist_ir_lifecycle():
    fig, ax = plt.subplots(figsize=(14, 8.6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.6)
    ax.axis('off')

    cx, cy = 7.0, 4.15
    box_w, box_h = 3.9, 1.55

    phases = {
        'prep': (5.05, 6.45, CYAN, TEXT_DARK,
                 'Preparation',
                 'plans, tooling, contacts\ntraining and exercises'),
        'detect': (9.35, 4.05, AMBER, TEXT_DARK,
                   'Detection &\nAnalysis',
                   'triage alerts, scope impact\ncollect and analyze evidence'),
        'contain': (5.05, 1.25, ROSE, TEXT_LIGHT,
                    'Containment, Eradication\n& Recovery',
                    'isolate, eradicate, restore\nvalidate a clean state'),
        'post': (0.75, 4.05, PURPLE, TEXT_LIGHT,
                 'Post-Incident\nActivity',
                 'lessons learned, root cause\nupdate detections and playbooks'),
    }

    for x, y, fc, tc, title, sub in phases.values():
        rounded_box(ax, x, y, box_w, box_h, title, fc,
                    text_color=tc, fontsize=12, subtext=sub)

    arrow(ax, (7.25, 6.45), (9.55, 5.55), color=AMBER, lw=2.4, ms=18,
          connectionstyle='arc3,rad=-0.05')
    arrow(ax, (9.35, 4.0), (7.8, 2.7), color=ROSE, lw=2.4, ms=18,
          connectionstyle='arc3,rad=-0.05')
    arrow(ax, (5.0, 1.65), (3.55, 3.15), color=PURPLE, lw=2.4, ms=18,
          connectionstyle='arc3,rad=-0.05')
    arrow(ax, (4.65, 5.15), (5.65, 6.45), color=CYAN, lw=2.4, ms=18,
          connectionstyle='arc3,rad=-0.05')

    circle = plt.Circle((cx, cy), 1.1, color=SURFACE, zorder=3)
    ax.add_patch(circle)
    ax.text(cx, cy + 0.17, 'Continuous', ha='center', va='center',
            color=TEXT_LIGHT, fontsize=11, fontweight='bold', zorder=4)
    ax.text(cx, cy - 0.12, 'IR cycle', ha='center', va='center',
            color=TEXT_LIGHT, fontsize=11, fontweight='bold', zorder=4)
    ax.text(cx, cy - 0.45, 'SP 800-61r2', ha='center', va='center',
            color=SLATE, fontsize=10, zorder=4)

    ax.text(7.0, 0.35,
            'Evidence handling, communications, severity triage, and executive reporting span every phase.',
            ha='center', fontsize=9, color=SLATE, style='italic')

    plt.title('The NIST Incident Response Lifecycle (SP 800-61r2)',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch12_nist_ir_lifecycle.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 12 figures...')
    create_soar_phishing_workflow()
    create_nist_ir_lifecycle()
    print('Chapter 12 figures generated successfully.')
