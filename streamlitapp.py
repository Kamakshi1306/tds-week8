import streamlit as st

def find_largest_number(num1, num2, num3):
    # Find the largest number among the three
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # Input for three numbers
    num1 = st.number_input("Enter the first number:", value=0, step=1)
    num2 = st.number_input("Enter the second number:", value=0, step=1)
    num3 = st.number_input("Enter the third number:", value=0, step=1)

    # Calculate button
    calculate_button = st.button("Find")
    
    # Handle button click
    if calculate_button:
        # Find the largest number
        result = find_largest_number(num1, num2, num3)

        # Display the result
        st.write(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
