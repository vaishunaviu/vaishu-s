import pandas as pd

uploaded = 'https://raw.githubusercontent.com/vaishunaviu/vaishu-s/main/DigitalAd_dataset.csv'

 
try:
    dataset = pd.read_csv(uploaded, on_bad_lines='skip')   
    print("Dataset loaded successfully!\n")
    print("Dataset Shape:", dataset.shape)  
    print("\nFirst 5 Rows of the Dataset:")
    print(dataset.head(5))   
except Exception as e:
    print(f"Error loading dataset: {e}")
x=dataset.iloc[:,:-1].values
print(x)    
