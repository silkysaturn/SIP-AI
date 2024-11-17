import streamlit as st
import auth_functions

## -------------------------------------------------------------------------------------------------
## Not logged in -----------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
if 'user_info' not in st.session_state:
    col1,col2,col3 = st.columns([1,2,1])

    # Authentication form layout
    do_you_have_an_account = col2.selectbox(label='Do you have an account?',options=('Yes','No','I forgot my password'))
    auth_form = col2.form(key='Authentication form',clear_on_submit=False)
    email = auth_form.text_input(label='Email')
    password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Yes','No'} else auth_form.empty()
    auth_notification = col2.empty()

    # Sign In
    if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Signing in'):
            auth_functions.sign_in(email,password)

    # Create Account
    elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Creating account'):
            auth_functions.create_account(email,password)

    # Password Reset
    elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Sending password reset link'):
            auth_functions.reset_password(email)

    # Authentication success and warning messages
    if 'auth_success' in st.session_state:
        auth_notification.success(st.session_state.auth_success)
        del st.session_state.auth_success
    elif 'auth_warning' in st.session_state:
        auth_notification.warning(st.session_state.auth_warning)
        del st.session_state.auth_warning

## -------------------------------------------------------------------------------------------------
## Logged in --------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------


else:
    # Sign out
    st.header('Sign out:')
    st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

    # Delete Account
    st.header('Delete account:')
    password = st.text_input(label='Confirm your password',type='password')
    st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')

    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    #-------------------------------------------------#

    ## AI INTERVIEW




    #-------------------------------------------------#


    # Sample Data
    data = pd.DataFrame({
        'Date': pd.date_range(start='1/1/2020', periods=100),
        'Value': np.random.randn(100).cumsum()
    })

    # Set the title of the app
    st.title("My Streamlit Dashboard")

    # Display data
    st.subheader("Sample Data")
    st.write(data.head())

    # Slider and display selected value
    slider_value = st.slider('Select a range of values', 0, 100, (25, 75))
    st.write(f'Selected range: {slider_value}')


    # Matplotlib Plot
    st.subheader("Seaborn Line Plot")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=data, x='Date', y='Value')
    st.pyplot(plt)

    # Sidebar
    st.sidebar.title("Sidebar Options")
    sidebar_option = st.sidebar.radio('Choose a view', ['View 1', 'View 2', 'View 3'])
    st.sidebar.write(f'Selected: {sidebar_option}')

    # Display Columns Layout
    col1, col2 = st.columns(2)

    with col1:
        st.header('Column 1')
        st.write('This is the first column.')

    with col2:
        st.header('Column 2')
        st.write('This is the second column.')

