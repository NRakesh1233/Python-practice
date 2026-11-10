
import streamlit as st

st.title("squre root calculater")

st.write("Hello, welcome to my first app!")

num = st.slider("Select a value", 0, 100, 50)

sqr = num ** 2
st.write(f"The square of {num} is {sqr}")

# x=input("Enter your name: ")                                                                   

# if x=="rakesh":
#         print("Welcome rakesh!!")

# x=int(input("Enter your name: "))
# if x%2==0:
#     print("even number")
# else:
#           print("odd number")


# print("india","pak", "usa",sep='-' )
# x={1,2,3,4,4,5}

# print(x)
# y=2+3j      
# print(y.real)
# print(y.imag)
# print(type(y))

# a=111
# print(a)

# for i in range(1,11):
#     print(i);
# for i in [1,3,4,5,55,6,6,43,433]:
#      print(i);  
# for i in "rakesh":
#      print(i)

# for i in {1,3,4,5,55,6,6,43,433}:
#      print(i)
             
                    
                     