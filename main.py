
import matplotlib.pyplot as plt
import numpy as np

print("hey there, this is the solution of our exercise")
def positiont(t):
 if 0 <= t < 2:
   x = 2*t
 elif 2 <= t <= 5:
   x = 2*(t - 2)
 else: 
  print("you can't see the value of X(t) because 0 ≤ t ≤ 5 ")
  x = None
  
 return x 
one = float(input("Q1: Enter the value of (t) To calculate X(t)"))
print(positiont(one))
two = str(input("Q2: you want to se the value of x(0), x(1), x(2), x(3) and x(5)? answer yes or no"))
if two == "yes":
  print("x(0) = ",positiont(0))
  print("x(1) = ",positiont(1))
  print("x(2) = ",positiont(2))
  print("x(3) = ",positiont(3))
  print("x(5) = ",positiont(5))

  t_vals = np.linspace(0, 5, 100)
  x_vals = [positiont(t) for t in t_vals]
  plt.figure(figsize=(7, 4))
  plt.plot(t_vals, x_vals, label='x(t) position', color='blue', linewidth=2)
  plt.title("Sensor Position x(t) over Time") 
  plt.xlabel("Temps t (s)")
  plt.ylabel("Position x(t) (m)")
  plt.grid(True, linestyle='--', alpha=0.7)
  plt.axhline(0, color='black', linewidth=0.5)
  plt.axvline(0, color='black', linewidth=0.5)
  plt.legend()
  plt.show()
elif two == "no":
 print("it's okay,thank you for your attention")
else:
 print("Answer yes or no ,Let's try again ") 
     
 


    
   
 
   
 
