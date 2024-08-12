from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

# Set the backend to 'Agg' for non-interactive plotting
plt.switch_backend('Agg')

def generate_chart(chart_type, data):
    """Generate a chart based on the specified type and data."""
    fig, ax = plt.subplots()

    # Filter out uncategorized entries
    data = [item for item in data if item.get('category') != 'Uncategorized']

    if chart_type == 'bar':
        x = [str(item.get('cooking_time', 'N/A')) for item in data]
        y = [int(item.get('count', 0)) for item in data]  # Ensure count is an integer
        categories = [item.get('category', 'Unknown') for item in data]  # Default to 'Unknown' if 'category' is missing
        
        bars = ax.bar(x, y, color='skyblue')

        # Adding category labels to bars
        for bar, category in zip(bars, categories):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.0, height,
                f'{height}',
                ha='center', va='bottom', fontsize=9, color='black'
            )
        
        ax.set_xlabel('Cooking Time (minutes)')
        ax.set_ylabel('Number of Recipes')
        ax.set_title('Recipes by Cooking Time')

    elif chart_type == 'pie':
        labels = [item.get('preparation', 'Unknown') for item in data]
        sizes = [int(item.get('count', 0)) for item in data]  # Ensure count is an integer
        categories = [item.get('category', 'Unknown') for item in data]  # Default to 'Unknown' if 'category' is missing
        
        # Combine preparation and category for labels
        combined_labels = [f'{label} ({category})' for label, category in zip(labels, categories)]
        
        # Use category to differentiate colors
        colors = plt.get_cmap('tab10').colors[:len(categories)]
        ax.pie(sizes, labels=combined_labels, autopct=lambda p: '{:.0f}'.format(p * sum(sizes) / 100), colors=colors)
        ax.set_title('Recipe Distribution by Preparation Time and Category')

    elif chart_type == 'line':
        categories = list(set(item.get('category', 'Unknown') for item in data))  # Extract unique categories
        
        for category in categories:
            category_data = [(item.get('created_at', 'N/A'), int(item.get('count', 0))) for item in data if item.get('category') == category]
            if category_data:
                dates, counts = zip(*category_data)
                ax.plot(dates, counts, marker='o', label=category)
        
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Recipes')
        ax.set_title('Recipes Over Time')
        ax.legend(title='Category')

    else:
        raise ValueError('Unknown chart type')

    # Save the plot to a BytesIO object and encode as base64 string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return img_str
