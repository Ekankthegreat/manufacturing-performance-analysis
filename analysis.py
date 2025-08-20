# Email: 24f1001581@ds.study.iitm.ac.in
import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
efficiency = [70.2, 72.01, 75.81, 81.46]
average = sum(efficiency) / len(efficiency)
industry_target = 90

print("Quarterly Efficiency:", efficiency)
print("Average Efficiency:", round(average, 2))  # Should be 74.87

# Plot trend vs target
plt.figure(figsize=(8,5))
plt.plot(quarters, efficiency, marker="o", label="Equipment Efficiency")
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (90)")
plt.axhline(y=average, color="g", linestyle=":", label=f"Average ({round(average,2)})")

plt.title("Equipment Efficiency Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate (%)")
plt.ylim(60, 95)
plt.legend()
plt.tight_layout()
plt.savefig("efficiency_trend.png")
plt.show()
