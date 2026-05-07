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
        ax.text(x + w / 2, y + h * 0.62, text, ha='center', va='center',
                color=text_color, fontsize=fontsize, fontweight='bold')
        ax.text(x + w / 2, y + h * 0.28, subtext, ha='center', va='center',
                color=text_color, fontsize=fontsize - 1)
    else:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
                color=text_color, fontsize=fontsize, fontweight='bold')


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16, ls='-'):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                 mutation_scale=ms, lw=lw, color=color,
                                 linestyle=ls))


def create_edr_vs_av():
    fig, ax = plt.subplots(figsize=(14.5, 8.5))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Left: Traditional AV
    rounded_box(ax, 0.4, 7.7, 6.5, 0.9, 'Traditional Antivirus',
                ROSE, fontsize=14)
    rounded_box(ax, 0.6, 5.6, 6.0, 1.8, 'Endpoint',
                SURFACE_ALT, fontsize=11,
                subtext='Local on-disk signature DB\nperiodic scheduled scan\nfile-hash matching')
    rounded_box(ax, 0.6, 3.8, 6.0, 1.4, 'Signature Update',
                AMBER, text_color=TEXT_DARK, fontsize=11,
                subtext='Daily / weekly DAT file\npushed from vendor cloud')
    rounded_box(ax, 0.6, 1.5, 6.0, 1.9, 'Detection Logic',
                SURFACE, fontsize=11,
                subtext='Known-bad hashes only\nNo behavior, no telemetry,\nno response — alert / quarantine')
    arrow(ax, (3.6, 5.6), (3.6, 5.2), color=AMBER)
    arrow(ax, (3.6, 3.8), (3.6, 3.4), color=ROSE)

    # Right: EDR
    rounded_box(ax, 7.6, 7.7, 6.5, 0.9, 'EDR (Endpoint Detection & Response)',
                CYAN, text_color=TEXT_DARK, fontsize=14)

    rounded_box(ax, 7.8, 6.0, 6.0, 1.5, 'Lightweight Agent',
                SURFACE_ALT, fontsize=11,
                subtext='Continuous syscall / process /\nnetwork / file telemetry')
    rounded_box(ax, 7.8, 4.0, 6.0, 1.6, 'Cloud Analytics Backend',
                PURPLE, text_color=TEXT_DARK, fontsize=11,
                subtext='Behavior models • ML detection\nMITRE ATT&CK mapping')
    rounded_box(ax, 7.8, 2.0, 6.0, 1.6, 'Automated Response',
                EMERALD, text_color=TEXT_DARK, fontsize=11,
                subtext='Isolate host • kill process • roll back\nremote forensics on demand')

    arrow(ax, (10.8, 6.0), (10.8, 5.6), color=PURPLE)
    arrow(ax, (10.8, 4.0), (10.8, 3.6), color=EMERALD)

    # Bottom note
    ax.text(7.25, 0.5,
            'Traditional AV asks "have I seen this file before?"  •  '
            'EDR asks "is this behavior consistent with an attack?"',
            ha='center', fontsize=11, color=SLATE, style='italic')

    plt.title('EDR vs. Traditional Antivirus',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch09_edr_vs_av.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_email_auth():
    fig, ax = plt.subplots(figsize=(14.5, 9))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Sender side
    rounded_box(ax, 0.3, 6.5, 2.5, 1.2, 'Sender Mail\nServer',
                SURFACE_ALT, fontsize=11,
                subtext='alice@example.com')

    # In transit
    rounded_box(ax, 5.8, 6.5, 3.2, 1.2, 'Email in transit',
                CYAN, text_color=TEXT_DARK, fontsize=11,
                subtext='Headers + body + DKIM signature')

    # Receiver side
    rounded_box(ax, 11.8, 6.5, 2.4, 1.2, 'Receiving\nMail Server',
                SURFACE_ALT, fontsize=11,
                subtext='gmail.com')

    arrow(ax, (2.8, 7.1), (5.8, 7.1))
    arrow(ax, (9.0, 7.1), (11.8, 7.1))

    # DNS at the top
    rounded_box(ax, 5.5, 8.4, 3.8, 0.7,
                'DNS for example.com  (TXT records)',
                PURPLE, text_color=TEXT_DARK, fontsize=10)

    # SPF
    rounded_box(ax, 0.3, 4.3, 4.3, 1.7, 'SPF',
                EMERALD, text_color=TEXT_DARK, fontsize=13,
                subtext='Lists IPs allowed to send\nfor example.com\n→ checks envelope-from IP')

    # DKIM
    rounded_box(ax, 5.0, 4.3, 4.5, 1.7, 'DKIM',
                AMBER, text_color=TEXT_DARK, fontsize=13,
                subtext='Sender signs headers + body\nwith private key\n→ public key in DNS')

    # DMARC
    rounded_box(ax, 9.9, 4.3, 4.3, 1.7, 'DMARC',
                ROSE, fontsize=13,
                subtext='Aligns SPF / DKIM with\nFrom: domain\n→ policy: none / quarantine / reject')

    # arrows from DNS to each
    arrow(ax, (6.5, 8.4), (2.5, 6.0), color=SLATE, lw=1.3, ls='--')
    arrow(ax, (7.4, 8.4), (7.2, 6.0), color=SLATE, lw=1.3, ls='--')
    arrow(ax, (8.3, 8.4), (12.0, 6.0), color=SLATE, lw=1.3, ls='--')

    # Receiver checks (bottom)
    rounded_box(ax, 0.5, 1.5, 13.5, 2.2, 'Receiving server validation',
                SURFACE, fontsize=12)

    checks = [
        (1.3,  '1. Look up SPF for the envelope-from domain.\n   Is the sending IP in the allowed list?'),
        (5.0,  '2. Verify the DKIM signature using the public\n   key found at <selector>._domainkey.<domain>.'),
        (9.0,  '3. Check DMARC alignment between the From:\n   domain and SPF / DKIM, then apply the\n   published policy (none / quarantine / reject).'),
    ]
    for x, txt in checks:
        ax.text(x, 2.3, txt, ha='left', va='center',
                color=TEXT_LIGHT, fontsize=9.8)

    # Bottom note
    ax.text(7.25, 0.7,
            'SPF authenticates the sending IP. DKIM authenticates the message. '
            'DMARC ties them to the visible From: domain and tells the receiver what to do on failure.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('How SPF, DKIM, and DMARC Prevent Email Spoofing',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch09_email_auth.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 9 figures...')
    create_edr_vs_av()
    create_email_auth()
    print('Chapter 9 figures generated successfully.')
