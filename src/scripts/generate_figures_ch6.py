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
    ax.text(x + w / 2, y + h * 0.62, text, ha='center', va='center', color=text_color,
            fontsize=fontsize, fontweight='bold')
    if subtext:
        ax.text(x + w / 2, y + h * 0.28, subtext, ha='center', va='center', color=text_color,
                fontsize=fontsize - 1)


def arrow(ax, start, end, color=SLATE, style='-|>', lw=2.0, ms=16):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=ms, lw=lw, color=color))


def create_secure_cicd_pipeline():
    fig, ax = plt.subplots(figsize=(15, 7.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 8)
    ax.axis('off')

    rounded_box(ax, 0.4, 5.7, 2.0, 1.1, 'Plan\nRequirements', SURFACE_ALT, subtext='Security + usability')
    rounded_box(ax, 2.8, 5.7, 2.0, 1.1, 'Code\nCommit', CYAN, text_color=TEXT_DARK, subtext='Lint + branch protection')
    rounded_box(ax, 5.2, 5.7, 2.2, 1.1, 'Build\nDependencies', PURPLE, text_color=TEXT_DARK, subtext='SCA + SBoM')
    rounded_box(ax, 7.8, 5.7, 2.2, 1.1, 'Test\nAssurance', EMERALD, text_color=TEXT_DARK, subtext='SAST, DAST, IAST, RASP')
    rounded_box(ax, 10.4, 5.7, 2.0, 1.1, 'Release\nGate', AMBER, text_color=TEXT_DARK, subtext='Risk sign-off')
    rounded_box(ax, 12.8, 5.7, 1.8, 1.1, 'Deploy', ROSE, subtext='Canary + rollback')

    for start_x, end_x in [(2.4, 2.8), (4.8, 5.2), (7.4, 7.8), (10.0, 10.4), (12.4, 12.8)]:
        arrow(ax, (start_x, 6.25), (end_x, 6.25), color=SLATE)

    rounded_box(ax, 2.0, 3.6, 2.0, 0.95, 'Unit Tests', SURFACE)
    rounded_box(ax, 4.4, 3.6, 2.0, 0.95, 'Integration Tests', SURFACE)
    rounded_box(ax, 6.8, 3.6, 2.0, 0.95, 'Regression Tests', SURFACE)
    rounded_box(ax, 9.2, 3.6, 2.0, 0.95, 'Automated Retest', SURFACE)
    rounded_box(ax, 11.6, 3.6, 2.0, 0.95, 'Canary Validation', SURFACE)

    for x in [3.0, 5.4, 7.8, 10.2, 12.6]:
        ax.plot([x, x], [5.65, 4.55], linestyle='--', color=SLATE, linewidth=1.5)

    rounded_box(ax, 1.2, 1.2, 3.5, 1.0, 'Supply Chain Controls', AMBER, text_color=TEXT_DARK,
                subtext='Dependency pinning, signed artifacts, provenance')
    rounded_box(ax, 5.5, 1.2, 3.5, 1.0, 'Policy as Code', CYAN, text_color=TEXT_DARK,
                subtext='Prevent misconfigs before release')
    rounded_box(ax, 9.8, 1.2, 3.8, 1.0, 'Continuous Improvement Loop', PURPLE, text_color=TEXT_DARK,
                subtext='Findings feed backlog + hardening')

    arrow(ax, (13.7, 5.55), (13.7, 2.3), color=ROSE)
    arrow(ax, (11.7, 2.2), (2.1, 2.2), color=SLATE, style='-|>', lw=1.8)
    arrow(ax, (2.1, 2.2), (1.4, 5.7), color=SLATE, style='-|>', lw=1.8)

    ax.text(7.5, 0.35, 'Secure SDLC means every pipeline stage has security checks, release gates, and feedback loops.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Integrating Security into the CI/CD Pipeline', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch06_secure_cicd_pipeline.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


def create_secure_measured_boot():
    fig, ax = plt.subplots(figsize=(14.5, 7))
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 8)
    ax.axis('off')

    rounded_box(ax, 0.5, 5.8, 2.2, 1.0, 'Power On', SURFACE_ALT, subtext='Immutable ROM starts chain')
    rounded_box(ax, 3.0, 5.8, 2.2, 1.0, 'Firmware\n(UEFI)', CYAN, text_color=TEXT_DARK, subtext='Signature checked')
    rounded_box(ax, 5.5, 5.8, 2.2, 1.0, 'Bootloader', PURPLE, text_color=TEXT_DARK, subtext='Verified hash')
    rounded_box(ax, 8.0, 5.8, 2.2, 1.0, 'Kernel + Drivers', EMERALD, text_color=TEXT_DARK, subtext='Trusted launch')
    rounded_box(ax, 10.5, 5.8, 2.2, 1.0, 'OS + EDR Agent', AMBER, text_color=TEXT_DARK, subtext='Runtime policies')

    for start_x, end_x in [(2.7, 3.0), (5.2, 5.5), (7.7, 8.0), (10.2, 10.5)]:
        arrow(ax, (start_x, 6.3), (end_x, 6.3), color=SLATE)

    rounded_box(ax, 1.4, 3.7, 4.0, 1.2, 'Secure Boot', ROSE,
                subtext='Blocks unsigned or tampered boot components')
    rounded_box(ax, 6.0, 3.7, 3.8, 1.2, 'Measured Boot', ROSE,
                subtext='Stores component hashes in TPM PCRs')
    rounded_box(ax, 10.2, 3.7, 3.4, 1.2, 'Remote Attestation', ROSE,
                subtext='Verifier checks TPM evidence before trust')

    arrow(ax, (3.0, 5.75), (3.4, 4.9), color=ROSE, lw=1.8)
    arrow(ax, (6.2, 5.75), (7.8, 4.9), color=ROSE, lw=1.8)
    arrow(ax, (11.5, 5.75), (12.0, 4.9), color=ROSE, lw=1.8)

    rounded_box(ax, 1.0, 1.3, 3.5, 1.0, 'TPM / HSM Root of Trust', SURFACE,
                subtext='Hardware-protected keys and measurements')
    rounded_box(ax, 5.0, 1.3, 3.2, 1.0, 'vTPM for VMs', SURFACE,
                subtext='Extends trust into virtual hardware')
    rounded_box(ax, 8.6, 1.3, 2.7, 1.0, 'SED + Host Encryption', SURFACE,
                subtext='Protects data at rest')
    rounded_box(ax, 11.7, 1.3, 2.2, 1.0, 'Tamper Response', SURFACE_ALT,
                subtext='Self-healing recovery path')

    ax.plot([6.0, 6.0], [3.65, 2.35], linestyle='--', color=SLATE, linewidth=1.3)
    ax.plot([12.0, 12.0], [3.65, 2.35], linestyle='--', color=SLATE, linewidth=1.3)

    ax.text(7.2, 0.35,
            'Secure Boot enforces code integrity. Measured Boot provides verifiable evidence of the boot chain.',
            ha='center', fontsize=10, color=SLATE, style='italic')

    plt.title('Secure Boot and Measured Boot Process', fontsize=16, fontweight='bold', pad=14)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'ch06_secure_measured_boot.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == '__main__':
    print('Generating Chapter 6 figures...')
    create_secure_cicd_pipeline()
    create_secure_measured_boot()
    print('Chapter 6 figures generated successfully.')
