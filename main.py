P_A = 0.001 
P_B_given_A = 0.99 
P_B_given_not_A = 0.01 
P_not_A = 1 - P_A
P_A_given_B = (P_B_given_A * P_A) / ((P_B_given_A * P_A) + (P_B_given_not_A * P_not_A))
print('R: ', P_A_given_B)
