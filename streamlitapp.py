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

    # Calculate button and Enter key handling
    if st.button("Find") or st.session_state.enter_pressed:
        # Find the largest number
        result = find_largest_number(num1, num2, num3)

        # Display the result
        st.write(f"The largest number is: {result}")

    # Listen for Enter key press
    st.script("document.addEventListener('keydown', function(e) {if (e.key === 'Enter') {window.streamlit.sessionState.enter_pressed = true;}});")

if __name__ == "__main__":
    main()
