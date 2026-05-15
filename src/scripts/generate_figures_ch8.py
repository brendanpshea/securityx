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


def create_pki_lifecycle():
    fig, ax = plt.subplots(figsize=(14.5, 9))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Top row: Issuance flow
    ax.text(7.25, 9.0, 'Issuance', ha='center', fontsize=13,
            fontweight='bold', color=DARK)

    rounded_box(ax, 0.3, 7.4, 2.4, 1.0, 'Subscriber',
                SURFACE_ALT, fontsize=11, subtext='(Server / User)')
    rounded_box(ax, 3.3, 7.4, 2.4, 1.0, 'Registration\nAuthority (RA)',
                PURPLE, text_color=TEXT_DARK, fontsize=10)
    rounded_box(ax, 6.3, 7.4, 2.4, 1.0, 'Issuing CA',
                CYAN, text_color=TEXT_DARK, fontsize=11,
                subtext='(Intermediate)')
    rounded_box(ax, 9.3, 7.4, 2.4, 1.0, 'Root CA',
                ROSE, fontsize=11, subtext='(Offline)')
    rounded_box(ax, 12.0, 7.4, 2.2, 1.0, 'Repository\n+ CRL / OCSP',
                EMERALD, text_color=TEXT_DARK, fontsize=10)

    # Issuance arrows
    arrow(ax, (2.7, 7.9), (3.3, 7.9))
    ax.text(3.0, 8.15, 'CSR', ha='center', fontsize=8.5, color=DARK)
    arrow(ax, (5.7, 7.9), (6.3, 7.9))
    ax.text(6.0, 8.15, 'verify', ha='center', fontsize=8.5, color=DARK)
    arrow(ax, (8.7, 7.9), (9.3, 7.9), color=ROSE, ls='--', lw=1.6)
    ax.text(9.0, 8.15, 'signs', ha='center', fontsize=8.5, color=DARK)
    arrow(ax, (11.7, 7.9), (12.0, 7.9))

    # Curved arrow returning the signed cert to the subscriber
    arrow(ax, (7.5, 7.4), (1.5, 7.4), color=EMERALD, lw=1.5,
          style='-|>', ms=14)
    ax.text(4.5, 7.05, 'signed certificate delivered',
            ha='center', fontsize=9, color=EMERALD, fontweight='bold')

    # Middle: TLS connection
    ax.text(7.25, 5.9, 'Use', ha='center', fontsize=13,
            fontweight='bold', color=DARK)
    rounded_box(ax, 1.3, 4.5, 3.0, 1.0, 'Server presents\nCertificate Chain',
                SURFACE_ALT, fontsize=10)
    rounded_box(ax, 5.5, 4.5, 3.4, 1.0, 'TLS Handshake',
                CYAN, text_color=TEXT_DARK, fontsize=11)
    rounded_box(ax, 10.1, 4.5, 3.0, 1.0, 'Browser / Client\n(Relying Party)',
                SURFACE_ALT, fontsize=10)

    arrow(ax, (4.3, 5.0), (5.5, 5.0))
    arrow(ax, (8.9, 5.0), (10.1, 5.0))

    # Bottom row: Validation steps performed by the relying party
    ax.text(7.25, 3.5, 'Validation (performed by the client)',
            ha='center', fontsize=13, fontweight='bold', color=DARK)

    steps = [
        ('1. Trust Chain',
         'Cert chains to a\ntrusted Root CA',
         CYAN),
        ('2. Signature',
         'Each cert signed by\nits issuer (CA pubkey)',
         PURPLE),
        ('3. Validity',
         'NotBefore / NotAfter\ndates are current',
         AMBER),
        ('4. Subject / SAN',
         'Hostname matches\nCN or SAN entry',
         EMERALD),
        ('5. Revocation',
         'CRL / OCSP /\nOCSP Stapling',
         ROSE),
    ]
    x = 0.3
    w = 2.7
    gap = 0.15
    for title, body, color in steps:
        rounded_box(ax, x, 1.4, w, 1.7, title, color,
                    text_color=TEXT_DARK if color != ROSE else TEXT_LIGHT,
                    fontsize=10, subtext=body)
        x += w + gap

    ax.text(7.25, 0.6,
            'If any check fails, the connection is aborted and the user sees a certificate warning.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('PKI Certificate Issuance and Validation',
              fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch08_pki_lifecycle.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_tls_handshake():
    fig, ax = plt.subplots(figsize=(14, 9.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Two columns: client and server
    rounded_box(ax, 1.5, 9.0, 3.5, 0.8, 'Client', CYAN,
                text_color=TEXT_DARK, fontsize=12)
    rounded_box(ax, 9.0, 9.0, 3.5, 0.8, 'Server', PURPLE,
                text_color=TEXT_DARK, fontsize=12)

    # Vertical lifelines
    ax.plot([3.25, 3.25], [2.0, 9.0], color=SLATE, lw=1.4, ls='--')
    ax.plot([10.75, 10.75], [2.0, 9.0], color=SLATE, lw=1.4, ls='--')

    # Messages: (y, direction, label, sub, color)
    messages = [
        (8.2, 'r', 'ClientHello',
         'supported ciphers, key share (X25519), random', CYAN),
        (7.2, 'l', 'ServerHello',
         'chosen cipher, key share, random', PURPLE),
        (6.4, 'l', '{Certificate}',
         'server cert chain (encrypted)', PURPLE),
        (5.7, 'l', '{CertificateVerify}',
         'proves possession of private key', PURPLE),
        (5.0, 'l', '{Finished}',
         'MAC over the handshake transcript', PURPLE),
        (4.0, 'r', '{Finished}',
         'client confirms keys match', CYAN),
        (3.0, 'b', 'Application Data',
         'AEAD-encrypted records (AES-GCM / ChaCha20-Poly1305)', EMERALD),
    ]

    for y, direction, label, sub, color in messages:
        if direction == 'r':
            arrow(ax, (3.4, y), (10.6, y), color=color, lw=2.0)
            tx = 7.0
        elif direction == 'l':
            arrow(ax, (10.6, y), (3.4, y), color=color, lw=2.0)
            tx = 7.0
        else:
            arrow(ax, (3.4, y), (10.6, y), color=color, lw=2.5)
            arrow(ax, (10.6, y - 0.25), (3.4, y - 0.25), color=color, lw=2.5)
            tx = 7.0
        ax.text(tx, y + 0.18, label, ha='center', fontsize=10.5,
                fontweight='bold', color=DARK)
        ax.text(tx, y - 0.15, sub, ha='center', fontsize=8.5,
                color=SLATE, style='italic')

    # Phase brackets on the left
    ax.text(0.7, 7.7, 'Key\nExchange', ha='center', va='center',
            fontsize=10, fontweight='bold', color=DARK,
            bbox=dict(boxstyle='round,pad=0.3', fc=AMBER, ec='white'))
    ax.text(0.7, 5.5, 'Server\nAuth', ha='center', va='center',
            fontsize=10, fontweight='bold', color=DARK,
            bbox=dict(boxstyle='round,pad=0.3', fc=PURPLE, ec='white'))
    ax.text(0.7, 4.0, 'Client\nFinish', ha='center', va='center',
            fontsize=10, fontweight='bold', color=TEXT_DARK,
            bbox=dict(boxstyle='round,pad=0.3', fc=CYAN, ec='white'))
    ax.text(0.7, 3.0, 'Encrypted\nTraffic', ha='center', va='center',
            fontsize=10, fontweight='bold', color=TEXT_DARK,
            bbox=dict(boxstyle='round,pad=0.3', fc=EMERALD, ec='white'))

    # Bottom note
    ax.text(7.0, 1.1,
            'TLS 1.3 completes the handshake in one round trip (1-RTT).\n'
            'Ephemeral (EC)DHE provides forward secrecy; the certificate authenticates the server but does not encrypt session keys.',
            ha='center', fontsize=9.5, color=SLATE, style='italic')

    plt.title('The TLS 1.3 Handshake', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch08_tls_handshake.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 8 figures...')
    create_pki_lifecycle()
    create_tls_handshake()
    print('Chapter 8 figures generated successfully.')
