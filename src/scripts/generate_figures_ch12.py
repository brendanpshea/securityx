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


def create_soar_phishing_workflow():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    # ---- Trigger row ----
    rounded_box(ax, 0.3, 8.8, 3.0, 1.1,
                'Email Gateway / SEG',
                SURFACE_ALT, fontsize=10,
                subtext='suspicious attachment\nor link detected')
    arrow(ax, (3.3, 9.35), (4.1, 9.35), color=SLATE, lw=1.6)
    rounded_box(ax, 4.1, 8.8, 3.2, 1.1,
                'SOAR Trigger',
                AMBER, text_color=TEXT_DARK, fontsize=11,
                subtext='Phishing Response\nPlaybook fires')
    arrow(ax, (7.3, 9.35), (8.1, 9.35), color=AMBER, lw=1.6)
    rounded_box(ax, 8.1, 8.8, 3.2, 1.1,
                'Header + URL Analysis',
                CYAN, text_color=TEXT_DARK, fontsize=10,
                subtext='extract IOCs, check\nVirusTotal / PhishTank')
    rounded_box(ax, 12.2, 8.8, 3.5, 1.1,
                'Threat Intel Lookup',
                PURPLE, fontsize=10,
                subtext='TIP / SIEM: known\ncampaign match?')
    arrow(ax, (11.3, 9.35), (12.2, 9.35), color=CYAN, lw=1.6)

    # ---- Decision diamond ----
    diamond_cx, diamond_cy = 7.0, 7.1
    diamond_pts = [(diamond_cx, diamond_cy + 0.75),
                   (diamond_cx + 1.3, diamond_cy),
                   (diamond_cx, diamond_cy - 0.75),
                   (diamond_cx - 1.3, diamond_cy)]
    diamond = plt.Polygon(diamond_pts, closed=True,
                          facecolor=ROSE, edgecolor='white', linewidth=1.8)
    ax.add_patch(diamond)
    ax.text(diamond_cx, diamond_cy, 'Malicious?', ha='center', va='center',
            color=TEXT_LIGHT, fontsize=10, fontweight='bold')
    ax.text(diamond_cx + 1.5, diamond_cy, 'YES', ha='left', va='center',
            color=ROSE, fontsize=9, fontweight='bold')
    ax.text(diamond_cx - 1.65, diamond_cy, 'NO →\nEscalate\nto analyst', ha='left', va='center',
            color=SLATE, fontsize=8)

    # Down arrow from intel lookup
    arrow(ax, (13.95, 8.8), (13.95, 7.85), color=PURPLE, lw=1.4)
    rounded_box(ax, 11.8, 6.8, 4.3, 1.0,
                'Score & Decide',
                SURFACE_ALT, fontsize=10,
                subtext='confidence score → auto or analyst')
    arrow(ax, (11.8, 7.3), (8.3, 7.1), color=SLATE, lw=1.4)

    # Down arrow from SOAR trigger to decision
    arrow(ax, (5.7, 8.8), (7.0, 7.85), color=AMBER, lw=1.4)

    # ---- Auto-response row ----
    arrow(ax, (8.3, 7.1), (10.0, 7.1), color=ROSE, lw=1.6)

    rounded_box(ax, 10.0, 6.55, 2.5, 1.1,
                'Auto-Quarantine',
                ROSE, fontsize=10,
                subtext='pull email from all\ninboxes (M365 / GSuite)')
    arrow(ax, (12.5, 7.1), (13.1, 7.1), color=ROSE, lw=1.4)
    rounded_box(ax, 13.1, 6.55, 2.6, 1.1,
                'Block IOCs',
                AMBER, text_color=TEXT_DARK, fontsize=10,
                subtext='push URLs/IPs to\nfirewall + DNS sinkhole')

    # ---- Triage / Notify row ----
    arrow(ax, (11.25, 6.55), (11.25, 5.6), color=ROSE, lw=1.4)
    rounded_box(ax, 9.6, 4.6, 3.3, 0.95,
                'Notify Reporter',
                SURFACE_ALT, fontsize=10,
                subtext='auto-reply to user with\nconfirmation + guidance')
    arrow(ax, (11.25, 4.6), (11.25, 3.6), color=SLATE, lw=1.4)
    rounded_box(ax, 9.6, 2.65, 3.3, 0.95,
                'Create SIEM Incident',
                CYAN, text_color=TEXT_DARK, fontsize=10,
                subtext='ticket, timeline, IOCs\nlinked to alert')

    # ---- Endpoint isolation branch ----
    arrow(ax, (14.4, 6.55), (14.4, 5.55), color=AMBER, lw=1.4)
    rounded_box(ax, 12.9, 4.6, 3.0, 0.95,
                'Scope: Any Clicks?',
                AMBER, text_color=TEXT_DARK, fontsize=10,
                subtext='EDR: link-click or\nattachment exec?')
    arrow(ax, (14.4, 4.6), (14.4, 3.6), color=ROSE, lw=1.6)
    rounded_box(ax, 12.9, 2.65, 3.0, 0.95,
                'Isolate Endpoint',
                ROSE, fontsize=10,
                subtext='EDR network-isolate\n+ alert SOC analyst')

    # ---- Post-incident ----
    arrow(ax, (10.75, 2.65), (10.75, 1.7), color=SLATE, lw=1.4)
    rounded_box(ax, 9.2, 0.75, 3.1, 0.95,
                'Post-Incident',
                EMERALD, text_color=TEXT_DARK, fontsize=10,
                subtext='metrics update • TIP IOC\nexport • runbook review')

    # ---- Legend ----
    rounded_box(ax, 0.3, 0.3, 1.2, 0.7, 'Automated', EMERALD,
                text_color=TEXT_DARK, fontsize=8)
    rounded_box(ax, 1.8, 0.3, 1.4, 0.7, 'Analyst Gate', SURFACE_ALT,
                fontsize=8)
    rounded_box(ax, 3.5, 0.3, 1.3, 0.7, 'Decision', ROSE, fontsize=8)

    ax.text(8.0, 0.15,
            'Steps in green/cyan/amber execute automatically within seconds. '
            'ROSE nodes require analyst confirmation or are escalation paths.',
            ha='center', fontsize=9, color=SLATE, style='italic')

    plt.title('Automated SOAR Phishing Response Workflow',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch12_soar_phishing.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_nist_ir_lifecycle():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    cx, cy = 7.0, 4.5
    radius = 2.8

    # ---- Four phase boxes arranged in a diamond/cycle ----
    phases = [
        (cx, cy + radius, CYAN, TEXT_DARK,
         'Preparation',
         'Policies • playbooks • tooling\ntraining • threat intel feeds\nIR team assembly'),
        (cx + radius * 1.05, cy, AMBER, TEXT_DARK,
         'Detection &\nAnalysis',
         'SIEM alerts • log triage\nIOC correlation • scoping\nmalware sandbox'),
        (cx, cy - radius, ROSE, TEXT_LIGHT,
         'Containment, Eradication\n& Recovery',
         'isolate hosts • block IOCs\nreimage • restore backups\nvalidate clean state'),
        (cx - radius * 1.05, cy, PURPLE, TEXT_LIGHT,
         'Post-Incident\nActivity',
         'lessons-learned meeting\nroot cause analysis\ndetection rule updates'),
    ]

    box_w, box_h = 3.4, 1.9
    centers = []
    for bx, by, fc, tc, title, sub in phases:
        lx = bx - box_w / 2
        ly = by - box_h / 2
        rounded_box(ax, lx, ly, box_w, box_h, title, fc,
                    text_color=tc, fontsize=12, subtext=sub)
        centers.append((bx, by))

    # ---- Cycle arrows between phases ----
    offsets = [
        ((centers[0][0] + 0.6, centers[0][1] - 0.9),
         (centers[1][0] - 0.8, centers[1][1] + 0.6), AMBER),
        ((centers[1][0] - 0.4, centers[1][1] - 0.9),
         (centers[2][0] + 0.8, centers[2][1] + 0.6), ROSE),
        ((centers[2][0] - 0.6, centers[2][1] + 0.9),
         (centers[3][0] + 0.7, centers[3][1] - 0.6), PURPLE),
        ((centers[3][0] + 0.4, centers[3][1] + 0.9),
         (centers[0][0] - 0.8, centers[0][1] - 0.6), CYAN),
    ]
    for start, end, col in offsets:
        arrow(ax, start, end, color=col, lw=2.2, ms=18)

    # ---- Center label ----
    circle = plt.Circle((cx, cy), 1.1, color=SURFACE, zorder=3)
    ax.add_patch(circle)
    ax.text(cx, cy + 0.18, 'NIST SP', ha='center', va='center',
            color=TEXT_LIGHT, fontsize=11, fontweight='bold', zorder=4)
    ax.text(cx, cy - 0.22, '800-61r2', ha='center', va='center',
            color=SLATE, fontsize=10, zorder=4)

    # ---- Supplemental detail boxes ----
    detail_items = [
        (0.3, 7.7, SURFACE_ALT, 'Key Prep Artifacts',
         '• IR Policy & plan\n• Contact lists\n• Jump bag / forensic kit\n• Tabletop exercises'),
        (10.4, 7.7, SURFACE_ALT, 'Severity Triage',
         '• P1 (Critical) < 15 min\n• P2 (High) < 1 hr\n• P3 (Medium) < 4 hr\n• P4 (Low) < 24 hr'),
        (0.3, 0.3, SURFACE_ALT, 'Chain of Custody',
         '• Hash all evidence\n• Maintain access log\n• Use write-blockers\n• Legal hold if needed'),
        (10.4, 0.3, SURFACE_ALT, 'Lessons-Learned Output',
         '• What happened / why\n• Detection gap fixed?\n• Playbook updated?\n• Exec summary'),
    ]
    for dx, dy, fc, title, body in detail_items:
        rounded_box(ax, dx, dy, 3.2, 1.6, title, fc, fontsize=9, subtext=body)

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
