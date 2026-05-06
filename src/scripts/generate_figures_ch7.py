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


def create_shared_responsibility():
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Column headers
    rounded_box(ax, 0.5, 8.4, 3.0, 0.7, 'On-Premises', SURFACE_ALT, fontsize=11)
    rounded_box(ax, 3.8, 8.4, 3.0, 0.7, 'IaaS', CYAN, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 7.1, 8.4, 3.0, 0.7, 'PaaS', PURPLE, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 10.4, 8.4, 3.0, 0.7, 'SaaS', EMERALD, text_color=TEXT_DARK, fontsize=11)

    # Layers from top (Data) to bottom (Physical)
    layers = [
        ('Data & Access',    [0, 0, 0, 0]),
        ('Applications',     [0, 0, 0, 1]),
        ('Runtime / OS',     [0, 0, 1, 1]),
        ('Virtualization',   [0, 1, 1, 1]),
        ('Servers',          [0, 1, 1, 1]),
        ('Storage',          [0, 1, 1, 1]),
        ('Networking',       [0, 1, 1, 1]),
        ('Physical Facility',[0, 1, 1, 1]),
    ]
    # 0 = customer (CYAN), 1 = provider (ROSE)

    y = 7.6
    h = 0.85
    for label, owners in layers:
        for col, owner in enumerate(owners):
            x = 0.5 + col * 3.3
            color = ROSE if owner == 1 else CYAN
            tcolor = TEXT_LIGHT if owner == 1 else TEXT_DARK
            text = 'Provider' if owner == 1 else 'Customer'
            rounded_box(ax, x, y, 3.0, h - 0.15, text, color, text_color=tcolor, fontsize=9)
        ax.text(0.3, y + (h - 0.15) / 2, label, ha='right', va='center',
                color=DARK, fontsize=10, fontweight='bold')
        y -= h

    # Legend
    rounded_box(ax, 3.5, 0.2, 2.5, 0.55, 'Customer Responsibility', CYAN, text_color=TEXT_DARK, fontsize=9)
    rounded_box(ax, 6.2, 0.2, 2.5, 0.55, 'Provider Responsibility', ROSE, fontsize=9)

    plt.title('The Cloud Shared Responsibility Model (IaaS / PaaS / SaaS)',
              fontsize=15, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch07_shared_responsibility.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_api_gateway():
    fig, ax = plt.subplots(figsize=(14.5, 8))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Clients on the left
    rounded_box(ax, 0.3, 6.5, 1.8, 0.9, 'Web App', SURFACE_ALT, fontsize=10)
    rounded_box(ax, 0.3, 5.0, 1.8, 0.9, 'Mobile App', SURFACE_ALT, fontsize=10)
    rounded_box(ax, 0.3, 3.5, 1.8, 0.9, 'Partner B2B', SURFACE_ALT, fontsize=10)
    rounded_box(ax, 0.3, 2.0, 1.8, 0.9, 'IoT Device', SURFACE_ALT, fontsize=10)

    # WAF / DDoS layer
    rounded_box(ax, 2.8, 3.5, 1.8, 3.5, 'WAF\n+\nDDoS\nProtection', ROSE, fontsize=11)

    # API Gateway (central)
    rounded_box(ax, 5.2, 2.3, 3.4, 5.4, 'API Gateway', CYAN, text_color=TEXT_DARK, fontsize=14)
    # Functions inside the gateway
    inner_funcs = [
        ('Authentication (OAuth / JWT)', 6.7),
        ('Authorization / Scopes',        6.0),
        ('Rate Limiting & Quotas',         5.3),
        ('Request Validation',             4.6),
        ('Logging / Tracing',              3.9),
        ('Routing / Versioning',           3.2),
    ]
    for text, ypos in inner_funcs:
        ax.text(6.9, ypos, '• ' + text, ha='center', va='center',
                color=TEXT_DARK, fontsize=9.5)

    # Backend services on the right
    rounded_box(ax, 9.3, 6.7, 2.3, 1.0, 'Auth Service',     PURPLE, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 9.3, 5.4, 2.3, 1.0, 'Orders API',       EMERALD, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 9.3, 4.1, 2.3, 1.0, 'Payments API',     AMBER, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 9.3, 2.8, 2.3, 1.0, 'Inventory Service', SURFACE_ALT, fontsize=10)

    # Identity / observability sidecar
    rounded_box(ax, 12.0, 5.4, 2.2, 1.0, 'Identity Provider', PURPLE, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 12.0, 4.1, 2.2, 1.0, 'SIEM / Logs',       SURFACE, fontsize=10)

    # Arrows: clients -> WAF -> Gateway -> backends
    for ypos in [6.95, 5.45, 3.95, 2.45]:
        arrow(ax, (2.1, ypos), (2.8, ypos), color=SLATE)
    arrow(ax, (4.6, 5.25), (5.2, 5.25), color=SLATE)
    for ypos in [7.2, 5.9, 4.6, 3.3]:
        arrow(ax, (8.6, 5.0), (9.3, ypos), color=SLATE, lw=1.6)

    # Gateway -> IdP and SIEM
    arrow(ax, (8.6, 5.9), (12.0, 5.9), color=PURPLE, lw=1.5)
    arrow(ax, (8.6, 4.6), (12.0, 4.6), color=SLATE, lw=1.5)

    # Bottom note
    ax.text(7.25, 1.3,
            'The API Gateway centralizes authentication, authorization, rate limiting, validation, and observability —\n'
            'so individual services can focus on business logic without re-implementing security controls.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('API Gateway Architecture', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch07_api_gateway.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 7 figures...')
    create_shared_responsibility()
    create_api_gateway()
    print('Chapter 7 figures generated successfully.')
