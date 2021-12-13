import streamlit as st
import pickle
import numpy as np

fi=open('modl.pkl','rb')
model=pickle.load(fi)
fi.close()

def predict():
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Insurance predictor </h1>
    </div>
    """
    #Age	Sex	AST	BIL	CHE	CREA	GGT	ALPmean	CHOLmean	ALBmean	PROTmean	ALTmean
    st.markdown(html_temp,unsafe_allow_html=True)
    h1=st.text_input('Age')
    h2=st.selectbox('sex',['male','female'])
    h3=st.text_input('BMI')
    h4=st.text_input('no.of children')
    h5=st.selectbox('smoker',['yes','no'])
    h6=st.selectbox('region',['south-east','south-west','north-west','north-east'])
   
    if h2=='female':
        gen=1;
    else:
        gen=0;
    if h5=='yes':
        sm=1
    else:
        sm=0;
    if h6=='south-east':
        region=2
    elif h6=='soth-west':
        region=3
    elif h6=='north-east':
        region=0
    else:
        region=1
    
       
    if st.button('Predict'):
        user_input =np.array([h1,gen,h3,h4,sm,region]).reshape(1,-1)
        user_input= user_input.astype(np.int64)
        result=model.predict(user_input)
        st.header('Insurance ammount {}'.format(result))
        
           
if __name__=='__main__':
    st.title('Insurance Predictor')
    st.text('\n')
    predict()
    
