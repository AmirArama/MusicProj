import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate cents from a frequency ratio
def ratio_to_cents(ratio):
    return 1200 * math.log2(ratio)

# Just Intonation intervals with ratios and cents
just_intervals = {
    'Unison': {'ratio_text': '1:1', 'ratio_value': 1.0, 'cents': ratio_to_cents(1.0)},
    'Minor Second': {'ratio_text': '16:15', 'ratio_value': 16/15, 'cents': ratio_to_cents(16/15)},
    'Major Second': {'ratio_text': '9:8', 'ratio_value': 9/8, 'cents': ratio_to_cents(9/8)},
    'Minor Third': {'ratio_text': '6:5', 'ratio_value': 6/5, 'cents': ratio_to_cents(6/5)},
    'Major Third': {'ratio_text': '5:4', 'ratio_value': 5/4, 'cents': ratio_to_cents(5/4)},
    'Perfect Fourth': {'ratio_text': '4:3', 'ratio_value': 4/3, 'cents': ratio_to_cents(4/3)},
    'Tritone': {'ratio_text': '45:32', 'ratio_value': 45/32, 'cents': ratio_to_cents(45/32)},
    'Perfect Fifth': {'ratio_text': '3:2', 'ratio_value': 3/2, 'cents': ratio_to_cents(3/2)},
    'Minor Sixth': {'ratio_text': '8:5', 'ratio_value': 8/5, 'cents': ratio_to_cents(8/5)},
    'Major Sixth': {'ratio_text': '5:3', 'ratio_value': 5/3, 'cents': ratio_to_cents(5/3)},
    'Minor Seventh': {'ratio_text': '9:5', 'ratio_value': 9/5, 'cents': ratio_to_cents(9/5)},
    'Major Seventh': {'ratio_text': '15:8', 'ratio_value': 15/8, 'cents': ratio_to_cents(15/8)},
    'Octave': {'ratio_text': '2:1', 'ratio_value': 2.0, 'cents': ratio_to_cents(2.0)}
}

# Equal Temperament intervals with ratios and cents
equal_temperament_intervals = {
    'Unison': {'ratio_text': '2^(0/12)', 'ratio_value': 2**(0/12), 'cents': 0},
    'Minor Second': {'ratio_text': '2^(1/12)', 'ratio_value': 2**(1/12), 'cents': 100},
    'Major Second': {'ratio_text': '2^(2/12)', 'ratio_value': 2**(2/12), 'cents': 200},
    'Minor Third': {'ratio_text': '2^(3/12)', 'ratio_value': 2**(3/12), 'cents': 300},
    'Major Third': {'ratio_text': '2^(4/12)', 'ratio_value': 2**(4/12), 'cents': 400},
    'Perfect Fourth': {'ratio_text': '2^(5/12)', 'ratio_value': 2**(5/12), 'cents': 500},
    'Tritone': {'ratio_text': '2^(6/12)', 'ratio_value': 2**(6/12), 'cents': 600},
    'Perfect Fifth': {'ratio_text': '2^(7/12)', 'ratio_value': 2**(7/12), 'cents': 700},
    'Minor Sixth': {'ratio_text': '2^(8/12)', 'ratio_value': 2**(8/12), 'cents': 800},
    'Major Sixth': {'ratio_text': '2^(9/12)', 'ratio_value': 2**(9/12), 'cents': 900},
    'Minor Seventh': {'ratio_text': '2^(10/12)', 'ratio_value': 2**(10/12), 'cents': 1000},
    'Major Seventh': {'ratio_text': '2^(11/12)', 'ratio_value': 2**(11/12), 'cents': 1100},
    'Octave': {'ratio_text': '2^(12/12)', 'ratio_value': 2**(12/12), 'cents': 1200}
}

# Ensure both dictionaries have the same intervals
interval_names = list(just_intervals.keys())

# Data for plotting
just_cents = [just_intervals[name]['cents'] for name in interval_names]
equal_cents = [equal_temperament_intervals[name]['cents'] for name in interval_names]
x = np.arange(len(interval_names))  # the label locations
width = 0.35  # the width of the bars

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(x - width/2, just_cents, width, label='Just Intonation', color='skyblue')
rects2 = ax.bar(x + width/2, equal_cents, width, label='Equal Temperament', color='salmon')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Intervals')
ax.set_ylabel('Cents')
ax.set_title('Comparison of Intervals: Just Intonation vs. Equal Temperament')
ax.set_xticks(x)
ax.set_xticklabels(interval_names, rotation=45, ha='right')
ax.legend()

# Add ratio text above bars
for rect, name in zip(rects1, interval_names):
    height = rect.get_height()
    ratio_text = just_intervals[name]['ratio_text']
    ax.annotate(f'{ratio_text}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

for rect, name in zip(rects2, interval_names):
    height = rect.get_height()
    ratio_text = equal_temperament_intervals[name]['ratio_text']
    ax.annotate(f'{ratio_text}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

fig.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('interval_comparison.png')
plt.show 
