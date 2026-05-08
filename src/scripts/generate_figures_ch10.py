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


def create_purdue_model():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Levels from top (enterprise/IT) to bottom (physical process)
    levels = [
        (5, 'Level 5 — Enterprise / Internet',
         'Public web, email, VPN, remote vendors',
         SURFACE_ALT),
        (4, 'Level 4 — Enterprise IT',
         'ERP, email, business apps, corporate AD',
         CYAN),
        ('DMZ', 'Industrial DMZ (iDMZ)',
         'Patch servers, jump hosts, historian replicas, AV updates',
         AMBER),
        (3, 'Level 3 — Operations & Control',
         'Plant historians, MES, OT domain controllers',
         PURPLE),
        (2, 'Level 2 — Supervisory Control',
         'HMI, SCADA servers, engineering workstations',
         EMERALD),
        (1, 'Level 1 — Basic Control',
         'PLCs, RTUs, DCS controllers',
         ROSE),
        (0, 'Level 0 — Physical Process',
         'Sensors, actuators, valves, motors, drives',
         SURFACE),
    ]

    y = 9.6
    h = 1.05
    for level, label, desc, color in levels:
        text_color = TEXT_DARK if color in (CYAN, AMBER, PURPLE, EMERALD) else TEXT_LIGHT
        rounded_box(ax, 1.5, y, 11.0, h - 0.15, label, color,
                    text_color=text_color, fontsize=11.5, subtext=desc)
        # left-side level chip
        ax.text(0.85, y + (h - 0.15) / 2, str(level),
                ha='center', va='center', color=DARK, fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='circle,pad=0.4', fc='white', ec=DARK, lw=1.6))
        y -= h

    # Right-side trust labels
    ax.text(13.0, 9.65 + (1.05 - 0.15) / 2, 'Untrusted',
            ha='left', fontsize=10, color=ROSE, fontweight='bold')
    ax.text(13.0, 9.65 - 1.05 + (1.05 - 0.15) / 2, 'IT',
            ha='left', fontsize=10, color=CYAN, fontweight='bold')
    ax.text(13.0, 9.65 - 2 * 1.05 + (1.05 - 0.15) / 2, 'Boundary',
            ha='left', fontsize=10, color=AMBER, fontweight='bold')
    ax.text(13.0, 9.65 - 3 * 1.05 + (1.05 - 0.15) / 2, 'OT',
            ha='left', fontsize=10, color=PURPLE, fontweight='bold')
    ax.text(13.0, 9.65 - 6 * 1.05 + (1.05 - 0.15) / 2, 'Safety\ncritical',
            ha='left', fontsize=10, color=ROSE, fontweight='bold')

    # Note
    ax.text(7.0, 0.4,
            'All north-south traffic between IT and OT must traverse the industrial DMZ — no direct connections. '
            'East-west traffic within OT is segmented further by zones and conduits (ISA/IEC 62443).',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('The Purdue Model for ICS Security Architecture',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch10_purdue_model.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_wireless_segmentation():
    fig, ax = plt.subplots(figsize=(14.5, 9))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Central wireless controller / firewall
    rounded_box(ax, 5.7, 4.0, 3.1, 1.4, 'Wireless\nController + FW',
                SURFACE_ALT, fontsize=12,
                subtext='802.1X / RADIUS  •  per-SSID VLAN')

    # Identity / RADIUS server
    rounded_box(ax, 6.0, 6.4, 2.5, 0.9, 'RADIUS / NPS',
                PURPLE, text_color=TEXT_DARK, fontsize=10)
    arrow(ax, (7.25, 6.4), (7.25, 5.4), color=PURPLE, lw=1.4)

    # SSIDs along the left
    ssids_left = [
        (7.2, 'Corp-Trusted',
         'WPA3-Enterprise (EAP-TLS)\nDevice cert + user MFA\nFull internal access', CYAN),
        (5.4, 'Corp-BYOD',
         'WPA3-Enterprise (EAP-TLS)\nMDM-managed only\nLimited app access', EMERALD),
        (3.6, 'Guest',
         'Captive portal\nInternet only — no internal\nClient isolation on', AMBER),
        (1.8, 'IoT / Smart-bldg',
         'WPA3-PSK per-device\nVLAN isolated, egress only\nto vendor cloud', ROSE),
    ]
    for y, name, desc, color in ssids_left:
        text_color = TEXT_DARK if color in (CYAN, EMERALD, AMBER) else TEXT_LIGHT
        rounded_box(ax, 0.3, y, 4.6, 1.4, name, color,
                    text_color=text_color, fontsize=11, subtext=desc)
        arrow(ax, (4.9, y + 0.7), (5.7, 4.7), color=SLATE, lw=1.3)

    # Destinations along the right
    rounded_box(ax, 9.6, 7.0, 4.5, 1.0, 'Internal Apps + AD',
                CYAN, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 9.6, 5.6, 4.5, 1.0, 'BYOD App Set (Intune)',
                EMERALD, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 9.6, 4.2, 4.5, 1.0, 'Internet only',
                AMBER, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 9.6, 2.8, 4.5, 1.0, 'Vendor Cloud (egress)',
                ROSE, fontsize=11)

    arrow(ax, (8.8, 4.7), (9.6, 7.5), color=CYAN, lw=1.4)
    arrow(ax, (8.8, 4.7), (9.6, 6.1), color=EMERALD, lw=1.4)
    arrow(ax, (8.8, 4.7), (9.6, 4.7), color=AMBER, lw=1.4)
    arrow(ax, (8.8, 4.7), (9.6, 3.3), color=ROSE, lw=1.4)

    # Note
    ax.text(7.25, 0.7,
            'Each SSID maps to its own VLAN, ACL set, and policy. The controller — not the radio — is the policy enforcement point.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Segmenting a Corporate Wireless Network',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch10_wireless_segmentation.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 10 figures...')
    create_purdue_model()
    create_wireless_segmentation()
    print('Chapter 10 figures generated successfully.')
