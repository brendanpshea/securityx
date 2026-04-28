import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import os

img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/assets/images'))
os.makedirs(img_dir, exist_ok=True)

def create_bcdr_lifecycle():
    fig, ax = plt.subplots(figsize=(10, 3.5))
    
    steps = [
        "1. Project\nInitiation",
        "2. Business Impact\nAnalysis (BIA)",
        "3. Recovery Strategy\nDevelopment",
        "4. Plan Design &\nImplementation",
        "5. Testing &\nMaintenance"
    ]
    
    colors = ["#1e293b", "#334155", "#475569", "#64748b", "#06b6d4"]
    text_colors = ["#f8fafc", "#f8fafc", "#f8fafc", "#f8fafc", "#0f172a"]
    
    spacing = 1.8
    box_width = 1.6
    box_height = 0.8
    
    for i, step in enumerate(steps):
        x = i * spacing
        y = 0
        
        # We can draw chevron-like boxes by using a custom polygon, or simple rounded boxes
        # Since standard Bbox is cleaner, let's use FancyBboxPatch 
        from matplotlib.patches import FancyBboxPatch
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height, 
                             boxstyle="round,pad=0.1", fc=colors[i], ec='white', lw=1.5)
        ax.add_patch(box)
        
        ax.text(x, y, step, ha='center', va='center', color=text_colors[i], fontsize=10, fontweight='bold')
        
        if i < len(steps) - 1:
            arrow = FancyArrowPatch((x + box_width/2 + 0.1, y), (x + spacing - box_width/2 - 0.1, y),
                                    arrowstyle='-|>', mutation_scale=15, color='#475569', lw=2)
            ax.add_patch(arrow)
            
    # Add an arrow looping from step 5 back to step 2 to show continuous improvement
    loop_arrow = FancyArrowPatch((4 * spacing, -box_height/2 - 0.1), 
                                 (1 * spacing, -box_height/2 - 0.1),
                                 connectionstyle="bar,fraction=-0.3",
                                 arrowstyle='-|>', mutation_scale=15, color='#06b6d4', lw=2, linestyle='--')
    ax.add_patch(loop_arrow)
    ax.text(2.5 * spacing, -1.2, "Continuous Improvement & Updates", ha='center', va='center', color='#06b6d4', fontsize=9, fontweight='bold')

    ax.set_xlim(-1, len(steps) * spacing - 0.5)
    ax.set_ylim(-1.5, 1)
    ax.axis('off')
    
    plt.title("The BCDR Planning Lifecycle", fontsize=15, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch02_bcdr_lifecycle.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating BCDR figure...")
    create_bcdr_lifecycle()
    print("Figures generated successfully!")
