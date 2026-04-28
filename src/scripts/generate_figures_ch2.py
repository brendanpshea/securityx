import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/assets/images'))
os.makedirs(img_dir, exist_ok=True)

def create_risk_workflow():
    fig, ax = plt.subplots(figsize=(10, 3))
    
    steps = [
        "1. Asset\nIdentification",
        "2. Threat\nIdentification",
        "3. Vulnerability\nIdentification",
        "4. Risk\nAnalysis",
        "5. Risk\nTreatment"
    ]
    
    colors = ["#1e293b", "#334155", "#475569", "#06b6d4", "#0f172a"]
    text_colors = ["#f8fafc", "#f8fafc", "#f8fafc", "#0f172a", "#f8fafc"]
    
    box_width = 1.6
    box_height = 0.8
    spacing = 2.0
    
    for i, step in enumerate(steps):
        x = i * spacing
        y = 0
        
        # Draw box
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height, 
                             boxstyle="round,pad=0.1", fc=colors[i], ec='white', lw=2)
        ax.add_patch(box)
        
        # Add text
        ax.text(x, y, step, ha='center', va='center', color=text_colors[i], fontsize=10, fontweight='bold')
        
        # Draw arrow to next step
        if i < len(steps) - 1:
            arrow = FancyArrowPatch((x + box_width/2 + 0.1, y), (x + spacing - box_width/2 - 0.1, y),
                                    arrowstyle='-|>', mutation_scale=15, color='#475569', lw=2)
            ax.add_patch(arrow)
            
    ax.set_xlim(-1, len(steps) * spacing - 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    plt.title("The Risk Assessment Workflow", fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch02_risk_workflow.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating figures...")
    create_risk_workflow()
    print("Figures generated successfully in docs/assets/images/")
