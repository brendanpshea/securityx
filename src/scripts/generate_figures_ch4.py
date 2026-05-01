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
    ax.text(x + w / 2, y + h * 0.60, text, ha='center', va='center', color=text_color,
            fontsize=fontsize, fontweight='bold')
    if subtext:
        ax.text(x + w / 2, y + h * 0.28, subtext, ha='center', va='center', color=text_color,
                fontsize=fontsize - 1)


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=ms, lw=lw, color=color))


def create_ha_architecture():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    rounded_box(ax, 0.6, 5.9, 2.0, 1.0, 'Internet Users', SURFACE_ALT)
    rounded_box(ax, 3.0, 5.9, 2.0, 1.0, 'CDN / Edge WAF', CYAN, text_color=TEXT_DARK)
    rounded_box(ax, 5.4, 5.9, 2.0, 1.0, 'Load Balancer', PURPLE, text_color=TEXT_DARK)
    rounded_box(ax, 8.0, 6.3, 1.9, 0.9, 'Web Tier A', SURFACE)
    rounded_box(ax, 8.0, 5.1, 1.9, 0.9, 'Web Tier B', SURFACE)
    rounded_box(ax, 10.5, 5.9, 2.0, 1.0, 'API Gateway', EMERALD, text_color=TEXT_DARK)
    rounded_box(ax, 10.5, 3.9, 2.0, 1.0, 'App Services', SURFACE)
    rounded_box(ax, 10.5, 1.8, 2.0, 1.0, 'Data Tier', ROSE)
    rounded_box(ax, 7.8, 1.8, 1.9, 1.0, 'Identity / PKI', AMBER, text_color=TEXT_DARK)
    rounded_box(ax, 5.4, 1.8, 1.8, 1.0, 'Log / SIEM', SURFACE_ALT)

    arrow(ax, (2.6, 6.4), (3.0, 6.4))
    arrow(ax, (5.0, 6.4), (5.4, 6.4))
    arrow(ax, (7.4, 6.4), (8.0, 6.75))
    arrow(ax, (7.4, 6.4), (8.0, 5.55))
    arrow(ax, (9.9, 6.4), (10.5, 6.4))
    arrow(ax, (11.5, 5.9), (11.5, 4.9))
    arrow(ax, (11.5, 3.9), (11.5, 2.8))
    arrow(ax, (9.7, 2.3), (10.5, 2.3), color=AMBER)
    arrow(ax, (7.2, 2.3), (7.8, 2.3), color=CYAN)
    arrow(ax, (6.3, 2.8), (6.3, 5.2), color=SLATE, style='<|-|>', ms=14)

    ax.text(6.35, 5.45, 'Telemetry\nfeeds', ha='center', va='bottom', fontsize=9, color=SLATE)
    ax.text(11.5, 7.55, 'Public Zone', ha='center', fontsize=10, fontweight='bold', color=SLATE)
    ax.text(11.5, 4.95, 'Application Zone', ha='center', fontsize=10, fontweight='bold', color=SLATE)
    ax.text(10.2, 0.85, 'Restricted Data Zone', ha='center', fontsize=10, fontweight='bold', color=SLATE)

    ax.plot([7.7, 12.8], [5.0, 5.0], linestyle='--', color=SLATE, linewidth=1.5)
    ax.plot([7.2, 12.8], [2.95, 2.95], linestyle='--', color=SLATE, linewidth=1.5)

    plt.title('High-Availability Enterprise Network Architecture', fontsize=16, fontweight='bold', pad=16)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch04_ha_architecture.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_load_balancing_diagram():
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(3.2, 6.3, 'Active-Active', fontsize=14, fontweight='bold', ha='center', color=DARK)
    ax.text(9.8, 6.3, 'Active-Passive', fontsize=14, fontweight='bold', ha='center', color=DARK)

    rounded_box(ax, 2.2, 5.1, 2.0, 0.9, 'Load Balancer', CYAN, text_color=TEXT_DARK)
    rounded_box(ax, 1.0, 3.5, 1.8, 0.9, 'Node A', SURFACE)
    rounded_box(ax, 3.6, 3.5, 1.8, 0.9, 'Node B', SURFACE)
    rounded_box(ax, 2.2, 1.7, 2.0, 0.8, 'Shared Health Checks', SURFACE_ALT)
    arrow(ax, (3.2, 5.1), (1.9, 4.4))
    arrow(ax, (3.2, 5.1), (4.5, 4.4))
    arrow(ax, (2.1, 3.5), (2.9, 2.5), color=EMERALD)
    arrow(ax, (4.3, 3.5), (3.5, 2.5), color=EMERALD)
    ax.text(3.2, 0.9, 'Traffic and failures are absorbed across both nodes.', ha='center', fontsize=9.5, color=SLATE)

    rounded_box(ax, 8.8, 5.1, 2.0, 0.9, 'Load Balancer', PURPLE, text_color=TEXT_DARK)
    rounded_box(ax, 7.6, 3.5, 1.8, 0.9, 'Active Node', SURFACE)
    rounded_box(ax, 10.2, 3.5, 1.8, 0.9, 'Passive Node', SURFACE_ALT)
    rounded_box(ax, 8.6, 1.7, 2.4, 0.8, 'Failover Trigger / Promotion', AMBER, text_color=TEXT_DARK)
    arrow(ax, (9.8, 5.1), (8.5, 4.4))
    arrow(ax, (9.8, 5.1), (11.1, 4.4), color=SLATE, lw=1.3)
    arrow(ax, (9.2, 3.5), (9.5, 2.5), color=EMERALD)
    arrow(ax, (10.6, 2.5), (11.1, 3.5), color=AMBER, style='-|>', lw=2.3)
    ax.text(9.8, 0.9, 'One node serves until health checks promote the standby node.', ha='center', fontsize=9.5, color=SLATE)

    plt.title('Active-Active vs. Active-Passive Load Balancing', fontsize=16, fontweight='bold', pad=16)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch04_load_balancing.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_dlp_layers_diagram():
    fig, ax = plt.subplots(figsize=(14, 6.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')

    rounded_box(ax, 0.8, 4.8, 2.2, 1.0, 'Endpoint Layer', SURFACE, subtext='Labeling, agent policy, copy controls')
    rounded_box(ax, 3.5, 4.8, 2.2, 1.0, 'Transit Layer', CYAN, text_color=TEXT_DARK, subtext='Email, web, CASB, proxy, API egress')
    rounded_box(ax, 6.2, 4.8, 2.2, 1.0, 'Cloud Layer', PURPLE, text_color=TEXT_DARK, subtext='SaaS sharing, tenant controls, discovery')
    rounded_box(ax, 8.9, 4.8, 2.2, 1.0, 'Data Layer', ROSE, subtext='Storage, DB, retention, encryption')
    rounded_box(ax, 11.6, 4.8, 1.6, 1.0, 'SOC / SIEM', SURFACE_ALT, subtext='Alerts')

    arrow(ax, (3.0, 5.3), (3.5, 5.3))
    arrow(ax, (5.7, 5.3), (6.2, 5.3))
    arrow(ax, (8.4, 5.3), (8.9, 5.3))
    arrow(ax, (11.1, 5.3), (11.6, 5.3))

    rounded_box(ax, 1.0, 2.3, 2.0, 0.8, 'Discover', AMBER, text_color=TEXT_DARK)
    rounded_box(ax, 4.1, 2.3, 2.0, 0.8, 'Classify', AMBER, text_color=TEXT_DARK)
    rounded_box(ax, 7.2, 2.3, 2.0, 0.8, 'Enforce', AMBER, text_color=TEXT_DARK)
    rounded_box(ax, 10.3, 2.3, 2.0, 0.8, 'Measure', AMBER, text_color=TEXT_DARK)
    arrow(ax, (3.0, 2.7), (4.1, 2.7), color=SLATE)
    arrow(ax, (6.1, 2.7), (7.2, 2.7), color=SLATE)
    arrow(ax, (9.2, 2.7), (10.3, 2.7), color=SLATE)

    for x in [1.9, 4.6, 7.3, 10.0, 12.4]:
        ax.plot([x, x], [4.75, 3.2], linestyle='--', color=SLATE, linewidth=1.3)

    ax.text(7.0, 0.9, 'Effective DLP is architectural: discover sensitive data, classify it, enforce policy across layers, and measure outcomes.',
            ha='center', fontsize=10, color=SLATE)

    plt.title('DLP Implementation Across Network Layers', fontsize=16, fontweight='bold', pad=16)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch04_dlp_layers.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 4 figures...')
    create_ha_architecture()
    create_load_balancing_diagram()
    create_dlp_layers_diagram()
    print('Chapter 4 figures generated successfully.')
