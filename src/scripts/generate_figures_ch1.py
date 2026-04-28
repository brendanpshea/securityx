import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os

# Ensure image directory exists
img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../docs/assets/images'))
os.makedirs(img_dir, exist_ok=True)

def create_hierarchy_pyramid():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Pyramid coordinates (bottom-left, bottom-right, top)
    # We will draw 4 horizontal slices
    # Layer 1: Procedures (Bottom)
    # Layer 2: Guidelines
    # Layer 3: Standards
    # Layer 4: Policies (Top)
    
    layers = [
        {"name": "Procedures", "desc": "Step-by-step instructions (How to)", "color": "#1e293b", "text_color": "#94a3b8"},
        {"name": "Guidelines", "desc": "Best practices & recommendations (Optional)", "color": "#334155", "text_color": "#cbd5e1"},
        {"name": "Standards", "desc": "Mandatory technical requirements (What)", "color": "#475569", "text_color": "#f1f5f9"},
        {"name": "Policies", "desc": "High-level rules & management intent (Why)", "color": "#06b6d4", "text_color": "#0f172a"}
    ]
    
    # Draw from bottom to top
    y_starts = [0, 2, 4, 6]
    y_ends = [2, 4, 6, 8]
    x_centers = 0
    widths_bottom = [8, 6, 4, 2]
    widths_top = [6, 4, 2, 0]
    
    for i in range(4):
        poly = Polygon([
            (-widths_bottom[i]/2, y_starts[i]), 
            (widths_bottom[i]/2, y_starts[i]), 
            (widths_top[i]/2, y_ends[i]), 
            (-widths_top[i]/2, y_ends[i])
        ], closed=True, facecolor=layers[i]["color"], edgecolor='white', linewidth=2)
        ax.add_patch(poly)
        
        # Add text
        ax.text(0, y_starts[i] + 1.2, layers[i]["name"], ha='center', va='center', 
                color=layers[i]["text_color"], fontsize=14, fontweight='bold')
        ax.text(0, y_starts[i] + 0.6, layers[i]["desc"], ha='center', va='center', 
                color=layers[i]["text_color"], fontsize=10)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-0.5, 8.5)
    ax.axis('off')
    
    plt.title("The Governance Documentation Hierarchy", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch01_governance_hierarchy.png'), dpi=300, transparent=False, facecolor='white')
    plt.close()

def create_raci_matrix():
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Table data
    columns = ["Task", "CISO", "SOC Analyst", "System Admin", "Legal Counsel", "PR Team"]
    cell_text = [
        ["Declare Security Incident", "A/R", "I", "I", "C", "I"],
        ["Contain the Breach", "A", "R", "R", "I", "I"],
        ["Analyze Malware", "A", "R", "I", "I", "I"],
        ["Notify Regulators", "A", "I", "I", "R", "C"],
        ["Issue Press Release", "A", "I", "I", "C", "R"]
    ]
    
    ax.axis('tight')
    ax.axis('off')
    
    table = ax.table(cellText=cell_text, colLabels=columns, loc='center', cellLoc='center')
    
    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)
    
    for (row, col), cell in table.get_celld().items():
        if col == 0:
            cell.set_width(0.3)
        else:
            cell.set_width(0.14)
            
        if row == 0:
            cell.set_facecolor('#0f172a')
            cell.set_text_props(color='white', weight='bold')
        elif col == 0:
            cell.set_facecolor('#1e293b')
            cell.set_text_props(color='white', weight='bold')
        else:
            # Color code RACI
            val = cell.get_text().get_text()
            if 'R' in val and 'A' not in val: cell.set_facecolor('#dcfce7') # Green for Responsible
            elif 'A' in val: cell.set_facecolor('#fee2e2') # Red for Accountable
            elif 'C' in val: cell.set_facecolor('#fef3c7') # Yellow for Consulted
            elif 'I' in val: cell.set_facecolor('#e0e7ff') # Blue for Informed
            
    plt.title("Example RACI Matrix for Incident Response", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, 'ch01_raci_matrix.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating figures...")
    create_hierarchy_pyramid()
    create_raci_matrix()
    print("Figures generated successfully in docs/assets/images/")
