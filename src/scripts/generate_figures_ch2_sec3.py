import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
import os

img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/assets/images'))
os.makedirs(img_dir, exist_ok=True)

def create_cyber_kill_chain():
    fig, ax = plt.subplots(figsize=(12, 4))
    
    steps = [
        "Reconnaissance",
        "Weaponization",
        "Delivery",
        "Exploitation",
        "Installation",
        "Command &\nControl (C2)",
        "Actions on\nObjectives"
    ]
    
    colors = ["#1e293b", "#334155", "#475569", "#64748b", "#94a3b8", "#cbd5e1", "#f8fafc"]
    text_colors = ["#f8fafc", "#f8fafc", "#f8fafc", "#f8fafc", "#0f172a", "#0f172a", "#0f172a"]
    
    box_width = 1.3
    box_height = 0.8
    spacing = 1.6
    
    for i, step in enumerate(steps):
        x = i * spacing
        y = 0
        
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height, 
                             boxstyle="round,pad=0.1", fc=colors[i], ec='#0f172a', lw=1.5)
        ax.add_patch(box)
        
        ax.text(x, y, step, ha='center', va='center', color=text_colors[i], fontsize=9, fontweight='bold')
        
        if i < len(steps) - 1:
            arrow = FancyArrowPatch((x + box_width/2 + 0.05, y), (x + spacing - box_width/2 - 0.05, y),
                                    arrowstyle='-|>', mutation_scale=12, color='#475569', lw=2)
            ax.add_patch(arrow)
            
    ax.set_xlim(-1, len(steps) * spacing - 0.5)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    plt.title("The Lockheed Martin Cyber Kill Chain", fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch02_cyber_kill_chain.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_diamond_model():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Diamond coordinates
    top = (0, 2)
    bottom = (0, -2)
    left = (-2, 0)
    right = (2, 0)
    
    # Draw edges
    ax.plot([left[0], top[0]], [left[1], top[1]], color='#94a3b8', lw=2, zorder=1)
    ax.plot([top[0], right[0]], [top[1], right[1]], color='#94a3b8', lw=2, zorder=1)
    ax.plot([right[0], bottom[0]], [right[1], bottom[1]], color='#94a3b8', lw=2, zorder=1)
    ax.plot([bottom[0], left[0]], [bottom[1], left[1]], color='#94a3b8', lw=2, zorder=1)
    
    # Draw nodes
    node_radius = 0.4
    nodes = {
        "Adversary": (top, "#ef4444", "#f8fafc"),    # Red
        "Victim": (bottom, "#3b82f6", "#f8fafc"),    # Blue
        "Capability": (left, "#10b981", "#f8fafc"),  # Green
        "Infrastructure": (right, "#f59e0b", "#f8fafc") # Yellow
    }
    
    for label, (pos, color, text_color) in nodes.items():
        circle = plt.Circle(pos, node_radius, color=color, zorder=2)
        ax.add_patch(circle)
        # Place text slightly offset
        y_offset = 0.6 if pos[1] > 0 else -0.6 if pos[1] < 0 else 0
        x_offset = 0.8 if pos[0] > 0 else -0.8 if pos[0] < 0 else 0
        
        ax.text(pos[0] + x_offset, pos[1] + y_offset, label, ha='center', va='center', 
                color='#0f172a', fontsize=12, fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=0.2))

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    
    plt.title("The Diamond Model of Intrusion Analysis", fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch02_diamond_model.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating Threat Modeling figures...")
    create_cyber_kill_chain()
    create_diamond_model()
    print("Figures generated successfully!")
