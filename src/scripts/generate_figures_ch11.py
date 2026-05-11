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


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16, ls='-'):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                 mutation_scale=ms, lw=lw, color=color,
                                 linestyle=ls))


def create_siem_pipeline():
    fig, ax = plt.subplots(figsize=(15, 8.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Sources on the left
    sources = [
        (7.4, 'Endpoints (EDR)'),
        (6.3, 'Firewalls / IDS'),
        (5.2, 'DNS / Proxy'),
        (4.1, 'Cloud / SaaS APIs'),
        (3.0, 'Identity (AD, IdP)'),
        (1.9, 'Applications'),
    ]
    for y, label in sources:
        rounded_box(ax, 0.3, y, 2.4, 0.85, label,
                    SURFACE_ALT, fontsize=10)
        arrow(ax, (2.7, y + 0.4), (3.6, y + 0.4), color=SLATE, lw=1.3)

    # Collection / Forwarders
    rounded_box(ax, 3.6, 1.9, 2.0, 6.4, 'Collectors\n+ Forwarders',
                AMBER, text_color=TEXT_DARK, fontsize=11,
                subtext='syslog, agents,\nAPI pollers')

    arrow(ax, (5.6, 5.1), (6.4, 5.1), lw=1.6)

    # Normalize / Parse
    rounded_box(ax, 6.4, 1.9, 2.0, 6.4, 'Normalize\n+ Enrich',
                CYAN, text_color=TEXT_DARK, fontsize=11,
                subtext='ECS / OCSF\nGeoIP, asset,\nuser context')

    arrow(ax, (8.4, 5.1), (9.2, 5.1), lw=1.6)

    # Index / Store
    rounded_box(ax, 9.2, 1.9, 2.0, 6.4, 'Index + Store',
                PURPLE, text_color=TEXT_DARK, fontsize=11,
                subtext='hot / warm / cold\nretention tiers')

    arrow(ax, (11.2, 5.1), (12.0, 5.1), lw=1.6)

    # Correlate + Detect
    rounded_box(ax, 12.0, 4.5, 2.7, 3.8, 'Correlate\n+ Detect',
                EMERALD, text_color=TEXT_DARK, fontsize=11,
                subtext='Rules • Sigma\nUEBA, ML')

    # Output: Alerts + Dashboards + Hunt
    rounded_box(ax, 12.0, 2.8, 2.7, 1.2, 'Alerts → SOAR', ROSE, fontsize=10)
    rounded_box(ax, 12.0, 1.5, 2.7, 1.0, 'Dashboards', SURFACE_ALT, fontsize=10)
    arrow(ax, (13.35, 4.5), (13.35, 4.0), color=ROSE, lw=1.4)

    # Bottom note
    ax.text(7.5, 0.7,
            'Garbage in, garbage out. Schema discipline at the normalize stage — ECS, OCSF, or a documented internal schema — '
            'is what makes everything downstream actually queryable.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('The SIEM Data Pipeline (Collection → Alerting)',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch11_siem_pipeline.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_honeynet():
    fig, ax = plt.subplots(figsize=(14.5, 9))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Attacker / internet on the left
    rounded_box(ax, 0.3, 4.5, 2.3, 1.0, 'Attacker /\nInternet',
                ROSE, fontsize=11)

    # Perimeter firewall
    rounded_box(ax, 3.1, 4.5, 1.8, 1.0, 'Perimeter\nFirewall',
                SURFACE_ALT, fontsize=10)
    arrow(ax, (2.6, 5.0), (3.1, 5.0), color=ROSE)

    # Real production network on top
    rounded_box(ax, 5.7, 6.5, 8.5, 1.5, 'Production Network',
                CYAN, text_color=TEXT_DARK, fontsize=12,
                subtext='workstations  •  servers  •  databases  •  real users')

    arrow(ax, (4.9, 5.5), (5.7, 6.7), color=SLATE)

    # Honeynet box at the bottom
    rounded_box(ax, 5.7, 0.8, 8.5, 4.5, 'Honeynet (isolated VLAN)',
                SURFACE, fontsize=12)

    arrow(ax, (4.9, 4.8), (5.7, 4.0), color=AMBER, lw=1.6)

    # Honeypots inside the honeynet
    rounded_box(ax, 6.1, 3.3, 2.4, 1.2, 'High-interaction\nHoneypot',
                EMERALD, text_color=TEXT_DARK, fontsize=10,
                subtext='Real OS, fake data')
    rounded_box(ax, 8.7, 3.3, 2.4, 1.2, 'Low-interaction\nHoneypot',
                AMBER, text_color=TEXT_DARK, fontsize=10,
                subtext='Cowrie / Dionaea')
    rounded_box(ax, 11.3, 3.3, 2.6, 1.2, 'Decoy Credentials\n+ Honey Tokens',
                PURPLE, text_color=TEXT_DARK, fontsize=10,
                subtext='Canary files, fake AWS keys')

    rounded_box(ax, 6.1, 1.5, 4.0, 1.2, 'Data Capture / Logger',
                SURFACE_ALT, fontsize=10,
                subtext='full pcap, syscall, keystroke')
    rounded_box(ax, 10.3, 1.5, 3.6, 1.2, 'SIEM / Analyst',
                ROSE, fontsize=10,
                subtext='alerts on ANY interaction')

    arrow(ax, (8.1, 3.3), (8.1, 2.7), color=SLATE, lw=1.4)
    arrow(ax, (10.1, 2.1), (10.3, 2.1), color=SLATE, lw=1.4)

    # Note
    ax.text(7.25, 0.3,
            'Any interaction with the honeynet is suspicious by definition — there are no legitimate users on these systems. '
            'High signal-to-noise ratio makes honeypots ideal threat-hunting telemetry.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Honeypot and Honeynet Architecture',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch11_honeynet.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 11 figures...')
    create_siem_pipeline()
    create_honeynet()
    print('Chapter 11 figures generated successfully.')
