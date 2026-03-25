import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def create_dashboard():
    print("\033[1;33m[EXECUTIVE DASHBOARD] Synthesizing 2026 Audit Report...\033[0m")
    
    fig = plt.figure(figsize=(16, 10), facecolor='black')
    plt.suptitle("Lauro Beck, DBA | 2026 Senior Architect Audit Summary", color='#BC8CF2', fontsize=20, fontweight='bold')

    # Subplot 1: Historical GP (Placeholder for the local PNG)
    ax1 = plt.subplot(2, 2, 1)
    if os.path.exists('IBM_GP.png'):
        img = mpimg.imread('IBM_GP.png')
        ax1.imshow(img)
    ax1.set_title("Historical Price Action (GP)", color='white')
    ax1.axis('off')

    # Subplot 2: Quantum Alpha (Placeholder for the QNTM PNG)
    ax2 = plt.subplot(2, 2, 2)
    if os.path.exists('IBM_Quantum_Weight.png'):
        img = mpimg.imread('IBM_Quantum_Weight.png')
        ax2.imshow(img)
    ax2.set_title("Quantum Portfolio Alpha (QNTM)", color='#BC8CF2')
    ax2.axis('off')

    # Subplot 3: Treasury Liquidity (Placeholder for the AISP PNG)
    ax3 = plt.subplot(2, 1, 2)
    if os.path.exists('Treasury_Liquidity_Audit.png'):
        img = mpimg.imread('Treasury_Liquidity_Audit.png')
        ax3.imshow(img)
    ax3.set_title("Consolidated Treasury Liquidity (AISP)", color='#113355')
    ax3.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('Final_Audit_Dashboard_2026.png', facecolor='black')
    print("\033[1;32m[COMPLETE]\033[0m Dashboard generated: Final_Audit_Dashboard_2026.png")

if __name__ == "__main__":
    create_dashboard()
