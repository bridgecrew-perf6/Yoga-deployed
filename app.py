from libraries import *
from home import *

from TadaAsana import *
from VrikshAsana import *
from TrikonaAsana import *
from ShavaAsana import *
from SetuBandhAsana import *
from PadahastAsana import *
from BhujangAsana import *
from ArdhChakrAsana import *

#loading the holistic model into our code
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

#defining the demo image which will be displayed as default
DEMO_IMAGE = 'demo.jpg'


#resizing the images
@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

#main Navigation of our application
with st.sidebar:
    selected = option_menu(
        menu_title="Free Your Chakras",
        options=["Home","Yoga Pose Grading","Meet the team"],
        icons=["house","bar-chart","person"],
        menu_icon='cast'

    )



if selected=='Home':
    home()  #function made in home.py



elif selected=='Yoga Pose Grading':

    app_mode = st.sidebar.selectbox('Choose the pose to perform',
    ['Tada Asana','Vriksha Asana','Trikona Asana','Shava Asana','SetuBandh Asana','Padahast Asana','Bhujanga Asana','Dhanur Asana'],)

    detection_mode = st.sidebar.selectbox('Grade through ',
        ['Image','Take Picture','Real Time Webcam'])


    if app_mode =='Tada Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            tadaAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            tadaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            tadaPicture()

    
    elif app_mode =='Vriksha Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            treeAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            treeVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            treePicture()

    elif app_mode =='Trikona Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            trikonaAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            trikonaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            trikonaPicture()


    elif app_mode =='Shava Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            shavaAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            shavaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            shavaPicture()

    elif app_mode =='SetuBandh Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            SetuBandhAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            SetuBandhAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            SetuBandhAsanaPicture()
        

    elif app_mode =='Padahast Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            PadahastAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            PadahastAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            PadahastAsanaPicture()


    elif app_mode =='Bhujanga Asana':

        
        st.title("Welcome !")
        st.title(f"Let's see how well you can perform {app_mode}")
        st.markdown('---')

        if detection_mode == "Image":
            BhujangAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            BhujangAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            BhujangAsanaPicture()

    else:

        st.title("Welcome !")
        st.title(f"Let's see how well you can perform Dhanur Asana")
        st.markdown('---')

        if detection_mode == "Image":
            ArdhChakrAsanaImage()  #function in TadaAsana.py

            

        if detection_mode == "Real Time Webcam":
            ArdhChakrAsanaVideo()  #function in TadaAsana.py

        if detection_mode == "Take Picture":

            ArdhChakrAsanaPicture()






        

                
                                        


         



            
            
            
            



            
                                            
                    

                    

                    

            

          

            
