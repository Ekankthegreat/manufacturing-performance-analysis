import matplotlib.pyplot as plt

# 📧 Email for verification
email = "24f1001581@ds.study.iitm.ac.in"

# Quarterly efficiency data
quarters = ["Q1", "Q2", "Q3", "Q4"]
efficiency = [70.2, 72.01, 75.81, 81.46]
industry_target = 90

# Calculate average
average_efficiency = sum(efficiency) / len(efficiency)
print(f"Frequency count (average efficiency): {average_efficiency:.2f}")

# Plot efficiency vs target
plt.figure(figsize=(8, 5))
plt.plot(quarters, efficiency, marker="o", label="Company Efficiency")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (90)")
plt.title("Quarterly Equipment Efficiency vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.legend()
plt.grid(True)

# Save chart
plt.savefig("chart.png")
plt.close()
