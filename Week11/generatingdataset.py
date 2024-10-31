import pandas as pd
import numpy as np

num_samples=1000

x1=np.random.choice(['A','B','C','D'],num_samples)
x2=np.random.choice(['W','X','Y','Z'],num_samples)

x3=np.random.normal(loc=50,scale=10,size=num_samples)
x4=np.random.uniform(0,100,size=num_samples)
x5=np.random.normal(loc=30,scale=5,size=num_samples)
x6=np.random.uniform(10,50,size=num_samples)
x7=np.random.uniform(0,1,size=num_samples)

y=np.random.choice([0,1],num_samples)

data=pd.DataFrame({
    'x1':x1,
    'x2':x2,
    'x3':x3,
    'x4':x4,
    'x5':x5,
    'x6':x6,
    'x7':x7,
    'y':y
})

data.to_csv("generated_demo.csv",index=False)

print("Dataset generated and saved as demo.csv")