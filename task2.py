import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Function to perform K-means clustering
def perform_clustering():
    try:
        num_clusters = int(cluster_entry.get())
        data = pd.read_csv(r'E:\prodegy\TASK2\PRODIGY_ML_02\Mall_Customers.csv')
        X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
        
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
        labels = kmeans.labels_
        
        plt.figure(figsize=(8, 6))
        plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, cmap='viridis')
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
        plt.xlabel('Annual Income (k$)')
        plt.ylabel('Spending Score (1-100)')
        plt.title('K-means Clustering')
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of clusters.")

# GUI Setup
root = tk.Tk()
root.title("Customer Segmentation")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Number of Clusters:").grid(column=0, row=0, sticky=tk.W)
cluster_entry = ttk.Entry(frame)
cluster_entry.grid(column=1, row=0)

cluster_button = ttk.Button(frame, text="Perform Clustering", command=perform_clustering)
cluster_button.grid(column=0, row=1, columnspan=2)

root.mainloop()
