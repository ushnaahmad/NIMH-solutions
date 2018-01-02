
<html>
    <div style = "display: inline-block; width=150px; height=75px;">
            <h2 style="text-align: center">NIMH Data Archive</h2>
        </div>
    <div>
        <div style="display: inline-block; width=150px; height=75px;">
            <img src="https://ndar.nih.gov/images/ndar/circuit_brain_red.png" alt="NIMH data archive image"/>            
        </div>        
	</div>
    <h2>Background</h2>
    <ul>
    <li>Joint initiative supported by NIMH, NICHD, NINDS, and NIEHS</li>
    <li>Contains data from a collection of repositories including the National Database for Autism Research (NDAR),  the RDoC Database (RDoCdb), the National Database for Clinical Trials related to Mental Illness (NDCT), and the NIH Pediatric MRI Repository (PedsMRI).</li>
    <li>Free data are available to the research community through a not too difficult application process</li>
    <li>Begun in late 2006, first data was received in 2008, significant data became available in 2012.</li>
    <li>Data submission every 6 months for NIMH awardees</li>
    </ul>
    
 <h2>Contact Us</h2>
<p>Email: NDAHelp@mail.nih.gov</p>
<p>Phone: 301-443-3265</p>

</html>    

<html>
    <h2>Some Numbers</h2>
    <div>
    <table align="left">
        <tr>
            <th>Data Type</th>
            <th>Subjects</th>
        </tr>
        <tr>
            <td>Clinical/Phenotype</td>
            <td>171,116</td>
        </tr>
                <tr>
            <td>EEG</td>
            <td>3,383</td>
        </tr>
        <tr>
            <td>Eye Tracking</td>
            <td>2,468</td>
        </tr>
        <tr>
            <td>fMRI</td>
            <td>8,256</td>
        </tr>
        <tr>
            <td>Genomics</td>
            <td>32,847</td>
        </tr>
        <tr>
            <td>Structural Imaging</td>
            <td>14,833</td>
        </tr>
    </table>
    </div>
    <div>

</html>  



<html>
<h2>New Projects</h2>
    <h3>Adolescent Brain Cognitive Development (ABCD) Study</h3>
    <ul>
    <li>Recruit 10,000 healthy children, ages 9 to 10 across the United States, and follow them into early adulthood.</li>
    <li>Use advanced brain imaging to observe brain growth with unprecedented precision.</li>
    <li>Examine how biology and environment interact and relate to developmental outcomes such as physical health, mental health, and life achievements including academic success</li>
    <li><a href="http://abcd-study.org/">Read more here...</a></li>
    </ul>
    <h3>Connectome Coordination Facility (CCF)</h3>
    <ul>
    <li>The CCF houses and distributes data for a series of studies focused on the connections within the human brain.</li>
    <li>The CCF currently supports 19 NIH-funded human connectome studies</li>
    <li>All data releases from the CCF studies will be made availble through the NIMH Data Archive </li>
    <li><a href="http://www.humanconnectome.org/about/project/">Read more here...</a></li></ul>
</html>

<html>
        
        <h2>NDA Search</h2>
        
      
    
        
        <p> A search tool available on the data archive <a href = "https://data-archive.nimh.nih.gov"> home page.</a> You can search by various categories, such as
    
           <ul><li>Content</li>
               <li>NDA Studies</li>
               <li/>Publications</li>
               <li>Collections</li>
               <li>Data Structures</li>
               <li>Data Elements</li>
               <li>Experiments</li>
               <li>Concepts</li></ul>
   
         You can also search by site.
           
           <ul><li>NDA</li>
               <li/>NDAR</li>
               <li>NDCT</li>
               <li>RDoCdb</li>
               <li>ABCD</li></ul>
    </p>
    
</html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Packaging Data</h2>
        <p>The next few slides will assume you have already queried your search and are ready for accessing the data files. </p>
        <p>For instructions and guidance on how to filter your cart and create a package to download, please refer to our <a href = "https://data-archive.nimh.nih.gov/training/training-modules"> training modules</a> on the NDA website.    
    
           <ul><li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.query.tools"> Query Tools </a></li>
   
           <li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.filter.cart" > Filter Cart </a></li>
           
           <li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.creating.package"> Create Package </a></ul></p>
    </div>
    
</html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Using Download Manager</h2>
            <p>Once a package has been created, data can be downloaded using the Download Manager tool. This tool is availabe to download at: https://ndar.nih.gov/DownloadManager.html (Note: not yet compatible with Java version 9).</p>    <p> For more information on how to use this tool, refer to the <a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.download.manager"> download manager training module </a>
    
      </div>
    
</html>


```python
import csv

reader =csv.reader(open('image03.txt',"r"), delimiter = '\t')

dm = []
for row in reader:
    for element in row:
        if element.startswith('s3'):
            print (element)
            dm.append(element)
```

    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Faces/NDARAB369MB6_image03_1373498869756.zip
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Faces/NDARAB369MB6_image03_1373498869756.jpg
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Hires/NDARAB369MB6_image03_1373497889885.zip
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Hires/NDARAB369MB6_image03_1373497889885.jpg
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/MPRAGE/NDARAB369MB6_image03_1373646986954.zip
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/MPRAGE/NDARAB369MB6_image03_1373646986954.jpg
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/RestingState/NDARAB369MB6_image03_1373502746757.zip
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/RestingState/NDARAB369MB6_image03_1373502746757.jpg
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Rewards/NDARAB369MB6_image03_1373507925274.zip
    s3://NDAR_Central/submission_9925/Project4/MIPAV Output/Rewards/NDARAB369MB6_image03_1373507925274.jpg
    s3://NDAR_Central/submission_9927/IS345_CCN.zip
    s3://NDAR_Central_1/submission_10080/BOLD-BioPoint.zip
    s3://NDAR_Central_1/submission_10080/BOLD-Faces.zip
    s3://NDAR_Central_1/submission_10080/BOLD-Language.zip
    s3://NDAR_Central_1/submission_10080/DTI.zip
    s3://NDAR_Central_1/submission_10080/MR.zip
    s3://NDAR_Central_1/submission_10080/RestingState.zip
    s3://NDAR_Central_1/submission_10080/T2.zip
    s3://NDAR_Central_1/submission_10080/localizer.zip
    s3://NDAR_Central_1/submission_10324/DTI/TD142C_DTI.tar
    s3://NDAR_Central_1/submission_10324/anat_hires/TD142C_anat_hires_new_RPI.nii.gz
    s3://NDAR_Central_1/submission_10324/anat_mprage/TD142C_anat_mprage_new_RPI.nii.gz
    s3://NDAR_Central_1/submission_10324/faces/TD142C_faces_new_RPI.nii.gz
    s3://NDAR_Central_1/submission_10324/resting6min/TD142C_resting6min_new_RPI.nii.gz
    s3://NDAR_Central_1/submission_10324/rewards_a/TD142C_rewards_a_new_RPI.nii.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCN383ZEE/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/MPRAGE_-_BWM_3.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARCY843HKN/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARDA952HKY/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDAREW988FK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFE295WPT/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_BioPoint_154_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Language__264_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Resting_State_165_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/DTI_64dir_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFU868CVF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARFX414AHK/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHK897GZX/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHU658FF2/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_11272/NDARHX274AFB/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_1/submission_11660/SSPS047_MPRAGE.nii.gz
    s3://NDAR_Central_1/submission_11660/SSPS057_MPRAGE.nii.gz
    s3://NDAR_Central_1/submission_11660/SSPS055_MPRAGE.nii.gz
    s3://NDAR_Central_1/submission_11660/SSPS033_MPRAGE.nii.gz
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/biopoint_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/AceFace_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11812/NDARFA755YRA/LangB_v3_3S_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARDA952HKY/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARDA952HKY/AceFace_NDARDA952HKY-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/biopoint_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/AceFace_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/LangB_v3_3S_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/resting_state_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFA755YRA/AceReward_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/BOLD_-_BioPoint_154_2.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/biopoint_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/AceFace_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/BOLD_-_Language__264_2.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/LangB_v4_2R_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/BOLD_-_Resting_State_165_2.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/resting_state_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFU868CVF/AceReward_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_11868/NDARFX414AHK/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_11868/NDARFX414AHK/resting_state_NDARFX414AHK-1.txt
    s3://NDAR_Central_1/submission_12528/NDARCY843HKN/localizer.tar.gz
    s3://NDAR_Central_1/submission_12528/NDARFA755YRA/localizer.tar.gz
    s3://NDAR_Central_1/submission_12528/NDARJC516JZF/localizer.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARCN383ZEE/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARCY843HKN/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARCY843HKN/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARCY843HKN/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARDA952HKY/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARDA952HKY/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARDG846PFF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDAREW988FK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARFA755YRA/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARFE295WPT/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARFE295WPT/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARFU868CVF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARFU868CVF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARHU658FF2/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARHX274AFB/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARHX274AFB/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARHX274AFB/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARJC516JZF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARJC516JZF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARJC516JZF/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARJZ207PA0/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARKC776CY3/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARKT871JV1/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARMN436JP7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARMN436JP7/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_1/submission_12532/NDARYM862JK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/biopoint_NDARCN383ZEE-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/AceFace_NDARCN383ZEE-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/resting_state_NDARCN383ZEE-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCN383ZEE/AceReward_NDARCN383ZEE-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/biopoint_NDARCY843HKN-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/resting_state_NDARCY843HKN-1.txt
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARCY843HKN/AceReward_NDARCY843HKN-1.txt
    s3://NDAR_Central_1/submission_12544/NDARDA952HKY/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARDA952HKY/AceFace_NDARDA952HKY-1.txt
    s3://NDAR_Central_1/submission_12544/NDARDA952HKY/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARDA952HKY/AceReward_NDARDA952HKY-1.txt
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/biopoint_NDAREW988FK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/AceFace_NDAREW988FK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/resting_state_NDAREW988FK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDAREW988FK7/AceReward_NDAREW988FK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/biopoint_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/AceFace_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFA755YRA/AceReward_NDARFA755YRA-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFE295WPT/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFE295WPT/biopoint_NDARFE295WPT-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/biopoint_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_BioPoint_154_2.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/AceFace_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Language__264_2.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/resting_state_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Resting_State_165_2.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/AceReward_NDARFU868CVF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARFU868CVF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/biopoint_NDARHU658FF2-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/AceFace_NDARHU658FF2-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/resting_state_NDARHU658FF2-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHU658FF2/AceReward_NDARHU658FF2-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/biopoint_NDARHX274AFB-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/AceFace_NDARHX274AFB-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/resting_state_NDARHX274AFB-1.txt
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARHX274AFB/AceReward_NDARHX274AFB-1.txt
    s3://NDAR_Central_1/submission_12544/NDARJC516JZF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARJC516JZF/biopoint_NDARJC516JZF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARJC516JZF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARJC516JZF/AceFace_NDARJC516JZF-1.txt
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/biopoint_NDARJZ207PA0-1.txt
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/AceFace_NDARJZ207PA0-1.txt
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARJZ207PA0/AceReward_NDARJZ207PA0-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/biopoint_NDARKC776CY3-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/AceFace_NDARKC776CY3-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/resting_state_NDARKC776CY3-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKC776CY3/AceReward_NDARKC776CY3-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/biopoint_NDARKT871JV1-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/AceFace_NDARKT871JV1-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/resting_state_NDARKT871JV1-1.txt
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARKT871JV1/AceReward_NDARKT871JV1-1.txt
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/biopoint_NDARMN436JP7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/AceFace_NDARMN436JP7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/resting_state_NDARMN436JP7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARMN436JP7/AceReward_NDARMN436JP7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/biopoint_NDARYM862JK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/AceFace_NDARYM862JK7-1.txt
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_1/submission_12544/NDARYM862JK7/resting_state_NDARYM862JK7-1.txt
    s3://NDAR_Central_1/submission_13592/NDARCN383ZEE/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARCY843HKN/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARDG846PFF/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARDR403NPK/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDAREN266GUL/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDAREW988FK7/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARFA755YRA/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARFE295WPT/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARFU868CVF/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARFX414AHK/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARHK897GZX/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARHU658FF2/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARHX274AFB/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARJZ207PA0/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARKC776CY3/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARKT871JV1/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARMN436JP7/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARNX466MBV/DTI_64dir.tar.gz
    s3://NDAR_Central_1/submission_13592/NDARYM862JK7/DTI_64dir.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001291/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/dti/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/dti/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019200001805/scanVisit__0192__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_imag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_imag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_real1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/B0_real1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/dti/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/dti/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001193/scanVisit__0003__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/dti/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/dti/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019100001183/scanVisit__0191__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001124/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001250/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_imag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/B0_real1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/019000001017/scanVisit__0190__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/002000001380/scanVisit__0020__0002/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_imag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_imag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_mag1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_mag1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_real1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/B0_real1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/dti/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/dti/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng3/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng3/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng4/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/gng4/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/restFA77/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/restFA77/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/t1/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/t1/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/t1_deface/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/t2/Native/Original__0001/DICOM.tar.gz
    s3://NDAR_Central_2/submission_11013/000300001549/scanVisit__0003__0001/MRI__0001/t2/Native/Original__0001/NIFTI4D.tar.gz
    s3://NDAR_Central_2/submission_11249/DTI/IS345B_CCN_DTI.zip
    s3://NDAR_Central_2/submission_11249/DTI/
    s3://NDAR_Central_2/submission_11249/anat_hires/IS345B_CCN_anat_hires_new_RPI.nii.gz
    s3://NDAR_Central_2/submission_11249/anat_hires/
    s3://NDAR_Central_2/submission_11249/anat_mprage/IS345B_CCN_anat_mprage_new_RPI.nii.gz
    s3://NDAR_Central_2/submission_11249/anat_mprage/
    s3://NDAR_Central_2/submission_11249/faces/IS345B_CCN_faces_new_RPI.nii.gz
    s3://NDAR_Central_2/submission_11249/faces/
    s3://NDAR_Central_2/submission_11249/resting6min/IS345B_CCN_resting6min_new_RPI.nii.gz
    s3://NDAR_Central_2/submission_11249/resting6min/
    s3://NDAR_Central_2/submission_11249/rewards_a/IS345B_CCN_rewards_a_new_RPI.nii.gz
    s3://NDAR_Central_2/submission_11249/rewards_a/
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARJC516JZF/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/DTI_64dir.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKC776CY3/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/DTI_64dir.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARKT871JV1/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/DTI_64dir.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_2/submission_11277/NDARMN436JP7/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/DTI_64dir.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_2/submission_11617/NDARFA755YRA/localizer.tar.gz
    s3://NDAR_Central_2/submission_11869/NDARHU658FF2/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_11869/NDARHU658FF2/LangB_v1_1R_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_11869/NDARHU658FF2/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_11869/NDARHU658FF2/resting_state_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_12037/NDAREB003RJ8/NDAREB003RJ8_addition_block_I_new.nii.gz
    s3://NDAR_Central_2/submission_12037/NDAREB003RJ8/NDAREB003RJ8_addblock_behavioral.edat
    s3://NDAR_Central_2/submission_12037/NDAREB003RJ8/NDAREB003RJ8_spgr_new_defaced.nii.gz
    s3://NDAR_Central_2/submission_12037/NDARFW514BBU/NDARFW514BBU_addition_block_I_new.nii.gz
    s3://NDAR_Central_2/submission_12037/NDARFW514BBU/NDARFW514BBU_addblock_behavioral.edat
    s3://NDAR_Central_2/submission_12037/NDARFW514BBU/NDARFW514BBU_spgr_new_defaced.nii.gz
    s3://NDAR_Central_2/submission_12037/NDARVM787WP6/NDARVM787WP6_addition_block_I_new.nii.gz
    s3://NDAR_Central_2/submission_12037/NDARVM787WP6/NDARVM787WP6_addblock_behavioral.edat
    s3://NDAR_Central_2/submission_12037/NDARVM787WP6/NDARVM787WP6_spgr_new_defaced.nii.gz
    s3://NDAR_Central_2/submission_12413/ELS_016_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_016_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_016_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_016_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_088_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_088_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_088_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_088_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_214_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_214_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_214_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_214_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_057_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_057_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_057_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_057_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_211_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_084_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_084_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_084_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_084_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_216_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_216_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_216_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_092_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_092_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_092_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_092_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_106_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_106_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_106_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_106_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_014_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_014_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_014_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_014_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_097_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_097_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_097_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_097_kidmid.nii
    s3://NDAR_Central_2/submission_12413/ELS_019_Conscious_Emo_Faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_019_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_2/submission_12413/ELS_019_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_2/submission_12413/ELS_019_kidmid.nii
    s3://NDAR_Central_2/submission_12529/NDARCN383ZEE/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARCY843HKN/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARCY843HKN/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARCY843HKN/MPRAGE_-_BWM_3.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARDA952HKY/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARDG846PFF/MPRAGE_-_BWM_FOV256.tar.gz
    s3://NDAR_Central_2/submission_12529/NDAREW988FK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARFA755YRA/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARFE295WPT/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARFU868CVF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARFU868CVF/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARHU658FF2/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARHX274AFB/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARJC516JZF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARJZ207PA0/MPRAGE_-_BWM_FOV256.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARKC776CY3/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARKT871JV1/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARMN436JP7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12529/NDARYM862JK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/biopoint_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/AceFace_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/LangB_v5_3U_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/resting_state_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARDG846PFF/AceReward_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_12553/NDARJZ207PA0/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_12553/NDARJZ207PA0/resting_state_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13581/NDARCY843HKN/localizer.tar.gz
    s3://NDAR_Central_2/submission_13581/NDARFA755YRA/localizer.tar.gz
    s3://NDAR_Central_2/submission_13581/NDARJC516JZF/localizer.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDG846PFF/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDG846PFF/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDG846PFF/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDR403NPK/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDR403NPK/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARDR403NPK/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_2/submission_13585/NDAREN266GUL/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_2/submission_13585/NDAREN266GUL/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_2/submission_13585/NDAREN266GUL/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARJZ207PA0/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARJZ207PA0/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARJZ207PA0/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARNX466MBV/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARNX466MBV/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_2/submission_13585/NDARNX466MBV/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/biopoint_NDARCN383ZEE-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/AceFace_NDARCN383ZEE-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/LangB_v1_1R_NDARCN383ZEE-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/resting_state_NDARCN383ZEE-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCN383ZEE/AceReward_NDARCN383ZEE-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/biopoint_NDARCY843HKN-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/AceFace_NDARCY843HKN-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/AceFace_NDARCY843HKN-2.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/LangB_v3_3S_NDARCY843HKN-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/resting_state_NDARCY843HKN-1.txt
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARCY843HKN/AceReward_NDARCY843HKN-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/AceFace_NDARDA952HKY-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/LangB_v8_1U_NDARDA952HKY-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDA952HKY/AceReward_NDARDA952HKY-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/biopoint_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/AceFace_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/LangB_v5_3U_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/resting_state_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDG846PFF/AceReward_NDARDG846PFF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/biopoint_NDARDR403NPK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/AceFace_NDARDR403NPK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/LangB_v6_1S_NDARDR403NPK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/resting_state_NDARDR403NPK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARDR403NPK/AceReward_NDARDR403NPK-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/biopoint_NDAREN266GUL-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/AceFace_NDAREN266GUL-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/LangB_v2_2U_NDAREN266GUL-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREN266GUL/AceReward_NDAREN266GUL-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/biopoint_NDAREW988FK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/AceFace_NDAREW988FK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/LangB_v8_1U_NDAREW988FK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/resting_state_NDAREW988FK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDAREW988FK7/AceReward_NDAREW988FK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/biopoint_NDARFA755YRA-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/AceFace_NDARFA755YRA-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/LangB_v3_3S_NDARFA755YRA-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/resting_state_NDARFA755YRA-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFA755YRA/AceReward_NDARFA755YRA-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/biopoint_NDARFE295WPT-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/AceFace_NDARFE295WPT-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFE295WPT/AceReward_NDARFE295WPT-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/biopoint_NDARFU868CVF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/AceFace_NDARFU868CVF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/LangB_v4_2R_NDARFU868CVF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/resting_state_NDARFU868CVF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFU868CVF/AceReward_NDARFU868CVF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/biopoint_NDARFX414AHK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/AceFace_NDARFX414AHK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/LangB_v2_2U_NDARFX414AHK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/resting_state_NDARFX414AHK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARFX414AHK/AceReward_NDARFX414AHK-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/biopoint_NDARHK897GZX-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/AceFace_NDARHK897GZX-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/LangB_v2_2U_NDARHK897GZX-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/resting_state_NDARHK897GZX-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHK897GZX/AceReward_NDARHK897GZX-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/biopoint_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/AceFace_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/LangB_v1_1R_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/resting_state_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHU658FF2/AceReward_NDARHU658FF2-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/biopoint_NDARHX274AFB-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/AceFace_NDARHX274AFB-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/LangB_v8_1U_NDARHX274AFB-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/resting_state_NDARHX274AFB-1.txt
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARHX274AFB/AceReward_NDARHX274AFB-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/biopoint_NDARJC516JZF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/AceFace_NDARJC516JZF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/LangB_v6_1S_NDARJC516JZF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/AceReward_NDARJC516JZF-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJC516JZF/AceReward_NDARJC516JZF-2.txt
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/biopoint_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/AceFace_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/LangB_v6_1S_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/resting_state_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARJZ207PA0/AceReward_NDARJZ207PA0-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/biopoint_NDARKC776CY3-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/AceFace_NDARKC776CY3-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/LangB_v7_3R_NDARKC776CY3-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/resting_state_NDARKC776CY3-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKC776CY3/AceReward_NDARKC776CY3-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/biopoint_NDARKT871JV1-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/AceFace_NDARKT871JV1-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/LangB_v3_3S_NDARKT871JV1-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/resting_state_NDARKT871JV1-1.txt
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARKT871JV1/AceReward_NDARKT871JV1-1.txt
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/biopoint_NDARMN436JP7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/AceFace_NDARMN436JP7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/LangB_v4_2R_NDARMN436JP7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/resting_state_NDARMN436JP7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARMN436JP7/AceReward_NDARMN436JP7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/biopoint_NDARNX466MBV-1.txt
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/AceFace_NDARNX466MBV-1.txt
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/LangB_v5_3U_NDARNX466MBV-1.txt
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/resting_state_NDARNX466MBV-1.txt
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARNX466MBV/AceReward_NDARNX466MBV-1.txt
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/biopoint_NDARYM862JK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/AceFace_NDARYM862JK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/LangB_v2_2U_NDARYM862JK7-1.txt
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_2/submission_13629/NDARYM862JK7/resting_state_NDARYM862JK7-1.txt
    s3://NDAR_Central_3/submission_11594/ELS_034_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_034_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_034_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_034_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_201_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_201_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_201_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_201_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_192_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_192_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_192_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_192_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_002_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_002_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_002_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_002_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_015_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_015_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_015_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_015_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_202_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_202_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_202_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_202_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_032_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_032_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_032_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_032_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_067_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_067_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_067_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_067_kidmid.nii
    s3://NDAR_Central_3/submission_11594/ELS_196_Conscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_196_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_3/submission_11594/ELS_196_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_3/submission_11594/ELS_196_kidmid.nii
    s3://NDAR_Central_3/submission_12206/SSPS063_MPRAGE.nii.gz
    s3://NDAR_Central_3/submission_12206/SSPS070_MPRAGE.nii.gz
    s3://NDAR_Central_3/submission_12322/cbta_project_anatomical_AN005_o1_v1_r1_a1_amri.zip
    s3://NDAR_Central_3/submission_12322/cbta_project_emoreg_AN005_o1_v1_r1_a1_fmri.zip
    s3://NDAR_Central_3/submission_12526/NDARDG846PFF/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_3/submission_12526/NDARDG846PFF/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_3/submission_12526/NDARDG846PFF/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_3/submission_12526/NDARJZ207PA0/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_3/submission_12526/NDARJZ207PA0/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_3/submission_12526/NDARJZ207PA0/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARCN383ZEE/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARCN383ZEE/LangB_v1_1R_NDARCN383ZEE-1.txt
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/AceFace_NDARCY843HKN-1.txt
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/AceFace_NDARCY843HKN-2.txt
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARCY843HKN/LangB_v3_3S_NDARCY843HKN-1.txt
    s3://NDAR_Central_3/submission_12546/NDARDA952HKY/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARDA952HKY/LangB_v8_1U_NDARDA952HKY-1.txt
    s3://NDAR_Central_3/submission_12546/NDAREW988FK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDAREW988FK7/LangB_v8_1U_NDAREW988FK7-1.txt
    s3://NDAR_Central_3/submission_12546/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFA755YRA/LangB_v3_3S_NDARFA755YRA-1.txt
    s3://NDAR_Central_3/submission_12546/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFA755YRA/resting_state_NDARFA755YRA-1.txt
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/AceFace_NDARFE295WPT-1.txt
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/LangB_v4_2R_NDARFE295WPT-2.txt
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFE295WPT/AceReward_NDARFE295WPT-1.txt
    s3://NDAR_Central_3/submission_12546/NDARFU868CVF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARFU868CVF/LangB_v4_2R_NDARFU868CVF-1.txt
    s3://NDAR_Central_3/submission_12546/NDARHU658FF2/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARHU658FF2/LangB_v1_1R_NDARHU658FF2-1.txt
    s3://NDAR_Central_3/submission_12546/NDARHX274AFB/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARHX274AFB/LangB_v5_3U_NDARHX274AFB-1.txt
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/LangB_v6_1S_NDARJC516JZF-1.txt
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/AceReward_NDARJC516JZF-1.txt
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARJC516JZF/AceReward_NDARJC516JZF-2.txt
    s3://NDAR_Central_3/submission_12546/NDARJZ207PA0/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARJZ207PA0/LangB_v6_1S_NDARJZ207PA0-1.txt
    s3://NDAR_Central_3/submission_12546/NDARKC776CY3/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARKC776CY3/LangB_v7_3R_NDARKC776CY3-1.txt
    s3://NDAR_Central_3/submission_12546/NDARKT871JV1/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARKT871JV1/LangB_v3_3S_NDARKT871JV1-1.txt
    s3://NDAR_Central_3/submission_12546/NDARMN436JP7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARMN436JP7/LangB_v4_2R_NDARMN436JP7-1.txt
    s3://NDAR_Central_3/submission_12546/NDARYM862JK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_12546/NDARYM862JK7/LangB_v2_2U_NDARYM862JK7-1.txt
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/biopoint_NDARTZ403TKU-1.txt
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/AceFace_NDARTZ403TKU-1.txt
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/resting_state_NDARTZ403TKU-1.txt
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/AceReward_NDARTZ403TKU-1.txt
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/DTI_64dir.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/DTI_64dir_ADC.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/DTI_64dir_FA.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/DTI_64dir_TRACEW.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARTZ403TKU/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/biopoint_NDARXZ339MZR-1.txt
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/AceFace_NDARXZ339MZR-1.txt
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/LangB_v8_1U_NDARXZ339MZR-1.txt
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/BOLD_-_Resting_State_240.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/resting_state_NDARXZ339MZR-1.txt
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/AceReward_NDARXZ339MZR-1.txt
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/DTI_64dir.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_3/submission_13674/NDARXZ339MZR/localizer.tar.gz
    s3://NDAR_Central_4/submission_10987/ELS_016_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_016_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_016_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_016_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_110_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_110_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_110_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_110_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_088_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_088_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_088_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_088_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_034_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_034_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_034_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_034_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_002_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_002_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_002_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_002_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_015_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_015_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_009_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_009_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_009_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_009_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_057_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_057_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_057_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_057_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_104_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_104_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_104_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_104_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_124_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_124_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_124_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_124_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_018_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_018_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_018_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_018_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_121_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_121_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_121_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_121_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_032_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_032_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_032_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_032_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_040_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_040_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_040_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_040_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_092_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_092_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_092_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_092_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_106_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_106_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_106_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_106_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_014_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_014_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_014_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_014_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_067_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_067_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_067_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_067_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_097_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_097_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_097_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_097_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_086_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_086_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_086_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_086_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_019_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_019_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_019_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_019_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_010_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_010_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_010_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_010_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_024_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_024_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_024_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_024_kidmid.nii
    s3://NDAR_Central_4/submission_10987/ELS_120_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_120_Nonconscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_10987/ELS_120_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_10987/ELS_120_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_152_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_152_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_152_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_152_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_146_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_146_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_146_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_146_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_171_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_171_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_171_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_171_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_162_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_162_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_162_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_162_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_164_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_164_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_164_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_164_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_151_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_151_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_151_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_151_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_132_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_132_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_132_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_132_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_170_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_170_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_170_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_170_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_129_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_129_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_129_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_163_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_163_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_163_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_163_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_156_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_156_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_156_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_156_kidmid.nii
    s3://NDAR_Central_4/submission_11179/ELS_188_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_11179/ELS_188_Conscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_188_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_11179/ELS_188_kidmid.nii
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_11275/NDARYM862JK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_11775/IS134_CCN_DTI.zip
    s3://NDAR_Central_4/submission_11775/IS134_CCN_anat_hires_new_RPI.nii.gz
    s3://NDAR_Central_4/submission_11775/IS134_CCN_anat_mprage_new_RPI.nii.gz
    s3://NDAR_Central_4/submission_11775/IS134_CCN_faces_new_RPI.nii.gz
    s3://NDAR_Central_4/submission_11775/IS134_CCN_resting8min_new_RPI.nii.gz
    s3://NDAR_Central_4/submission_11775/IS134_CCN_rewards_a_new_RPI.nii.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/resting_state_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/AceReward_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_11823/NDARFA755YRA/localizer.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/biopoint_NDARCN383ZEE-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/AceFace_NDARCN383ZEE-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/LangB_v1_1R_NDARCN383ZEE-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/resting_state_NDARCN383ZEE-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/AceReward_NDARCN383ZEE-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCN383ZEE/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/biopoint_NDARCY843HKN-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/AceFace_NDARCY843HKN-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/AceFace_NDARCY843HKN-2.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/LangB_v3_3S_NDARCY843HKN-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/resting_state_NDARCY843HKN-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/AceReward_NDARCY843HKN-1.txt
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/MPRAGE_-_BWM_3.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARCY843HKN/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/AceFace_NDARDA952HKY-1.txt
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/LangB_v8_1U_NDARDA952HKY-1.txt
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/AceReward_NDARDA952HKY-1.txt
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARDA952HKY/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/biopoint_NDAREW988FK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/AceFace_NDAREW988FK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/LangB_v8_1U_NDAREW988FK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/resting_state_NDAREW988FK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/AceReward_NDAREW988FK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDAREW988FK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/biopoint_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/AceFace_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/LangB_v3_3S_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/BOLD_-_Resting_State_240_8min.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/resting_state_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/AceReward_NDARFA755YRA-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFA755YRA/localizer.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/biopoint_NDARFE295WPT-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/AceFace_NDARFE295WPT-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/LangB_v4_2R_NDARFE295WPT-2.txt
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/AceReward_NDARFE295WPT-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFE295WPT/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/biopoint_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/AceFace_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/LangB_v4_2R_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/resting_state_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/AceReward_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/DTI_64dir_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_BioPoint_154_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/biopoint_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Faces_172_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/AceFace_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Language__264_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/LangB_v4_2R_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Resting_State_165_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/resting_state_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFU868CVF/AceReward_NDARFU868CVF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/biopoint_NDARFX414AHK-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/AceFace_NDARFX414AHK-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/LangB_v2_2U_NDARFX414AHK-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/resting_state_NDARFX414AHK-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/AceReward_NDARFX414AHK-1.txt
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARFX414AHK/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/biopoint_NDARHK897GZX-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/AceFace_NDARHK897GZX-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/LangB_v2_2U_NDARHK897GZX-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/resting_state_NDARHK897GZX-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/AceReward_NDARHK897GZX-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHK897GZX/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/biopoint_NDARHU658FF2-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/AceFace_NDARHU658FF2-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/LangB_v1_1R_NDARHU658FF2-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/resting_state_NDARHU658FF2-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/AceReward_NDARHU658FF2-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHU658FF2/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/biopoint_NDARHX274AFB-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/AceFace_NDARHX274AFB-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/LangB_v5_3U_NDARHX274AFB-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/resting_state_NDARHX274AFB-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/AceReward_NDARHX274AFB-1.txt
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARHX274AFB/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/biopoint_NDARJC516JZF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/AceFace_NDARJC516JZF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/LangB_v6_1S_NDARJC516JZF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/AceReward_NDARJC516JZF-1.txt
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/BOLD_-_Social_Reward_150_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/AceReward_NDARJC516JZF-2.txt
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARJC516JZF/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/biopoint_NDARKC776CY3-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/AceFace_NDARKC776CY3-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/LangB_v7_3R_NDARKC776CY3-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/resting_state_NDARKC776CY3-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/AceReward_NDARKC776CY3-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKC776CY3/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/biopoint_NDARKT871JV1-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/AceFace_NDARKT871JV1-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/LangB_v3_3S_NDARKT871JV1-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/resting_state_NDARKT871JV1-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/AceReward_NDARKT871JV1-1.txt
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARKT871JV1/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/biopoint_NDARMN436JP7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/AceFace_NDARMN436JP7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/LangB_v4_2R_NDARMN436JP7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/resting_state_NDARMN436JP7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/BOLD_-_Social_Reward_150.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/AceReward_NDARMN436JP7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARMN436JP7/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/BOLD_-_BioPoint_154.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/biopoint_NDARYM862JK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/BOLD_-_Faces_172.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/AceFace_NDARYM862JK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/BOLD_-_Language__264.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/LangB_v2_2U_NDARYM862JK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/BOLD_-_Resting_State_165.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/resting_state_NDARYM862JK7-1.txt
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_12015/NDARYM862JK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARCN383ZEE/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARCY843HKN/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARDG846PFF/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDAREW988FK7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARFA755YRA/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARFE295WPT/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARFU868CVF/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARFU868CVF/DTI_64dir_2.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARHU658FF2/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARHX274AFB/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARJZ207PA0/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARKC776CY3/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARKT871JV1/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARMN436JP7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_12527/NDARYM862JK7/DTI_64dir.tar.gz
    s3://NDAR_Central_4/submission_13167/ELS_110_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_110_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_110_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_110_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_104_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_104_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_104_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_104_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_132_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_132_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_132_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_132_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_086_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_086_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_086_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_086_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_163_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_163_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_163_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_163_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_024_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_024_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_024_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_024_kidmid.nii
    s3://NDAR_Central_4/submission_13167/ELS_120_Conscious_Emo_Faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_120_Nonconscious_Emo_faces.nii
    s3://NDAR_Central_4/submission_13167/ELS_120_T1w_9mm_sag_raw.nii
    s3://NDAR_Central_4/submission_13167/ELS_120_kidmid.nii
    s3://NDAR_Central_4/submission_13539/CBTA_anatomical_AN005_o1_v1_r1_a1_amri.zip
    s3://NDAR_Central_4/submission_13539/CBTA_biopoint_AN005_o1_v1_r1_a1_fmri.zip
    s3://NDAR_Central_4/submission_13539/CBTA_emoreg_AN005_o1_v1_r1_a1_fmri.zip
    s3://NDAR_Central_4/submission_13539/CBTA_anatomical_AN013_o1_v1_r1_a1_amri.zip
    s3://NDAR_Central_4/submission_13539/CBTA_biopoint_AN013_o1_v1_r1_a1_fmri.zip
    s3://NDAR_Central_4/submission_13539/CBTA_emoreg_AN013_o1_v1_r1_a1_fmri.zip
    s3://NDAR_Central_4/submission_13583/NDARCN383ZEE/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARCY843HKN/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARCY843HKN/MPRAGE_-_BWM_2.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARCY843HKN/MPRAGE_-_BWM_3.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARDA952HKY/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARDG846PFF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARDR403NPK/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDAREN266GUL/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDAREW988FK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARFA755YRA/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARFE295WPT/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARFU868CVF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARFX414AHK/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARHK897GZX/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARHU658FF2/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARHX274AFB/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARJC516JZF/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARJZ207PA0/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARKC776CY3/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARKT871JV1/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARMN436JP7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARNX466MBV/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13583/NDARYM862JK7/MPRAGE_-_BWM.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARCN383ZEE/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARCY843HKN/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARCY843HKN/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARCY843HKN/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARDA952HKY/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARDA952HKY/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARDG846PFF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARDR403NPK/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDAREN266GUL/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDAREW988FK7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARFA755YRA/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARFE295WPT/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARFE295WPT/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARFU868CVF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARFX414AHK/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARHK897GZX/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARHU658FF2/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARHX274AFB/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARHX274AFB/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARHX274AFB/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARJC516JZF/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARJC516JZF/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARJC516JZF/T2-AX__In-plane_Structural_3.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARJZ207PA0/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARKC776CY3/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARKT871JV1/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARMN436JP7/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARMN436JP7/T2-AX__In-plane_Structural_2.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARNX466MBV/T2-AX__In-plane_Structural.tar.gz
    s3://NDAR_Central_4/submission_13591/NDARYM862JK7/T2-AX__In-plane_Structural.tar.gz



```python
#Download Manager as a Webservice

import requests
import xml.etree.ElementTree as ET
from getpass import getpass

url = 'https://ndar.nih.gov/DataManager/dataManager'
username = input('Enter your NIMH Data Archives username:')
password = getpass('Enter your NIMH Data Archives password:')
package = input('Enter package ID:') #ex: 108728, 108335, 108772

payload = ('<?xml version="1.0" ?>\n'+
           '<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">\n' +
           '<S:Body> <ns3:QueryPackageFileElement\n' +
               'xmlns:ns4="http://dataManagerService"\n' +
               'xmlns:ns3="http://gov/nih/ndar/ws/datamanager/server/bean/jaxb"\n'+
               'xmlns:ns2="http://dataManager/transfer/model">\n' +
                   '<packageId>' + package +'</packageId>\n' +
                   '<associated>true</associated>\n' +
               '</ns3:QueryPackageFileElement>\n' +
           '</S:Body>\n' +
           '</S:Envelope>')


headers = {
    'Content-Type': "text/xml"
    }

r = requests.request("POST", url, data=payload, headers=headers)

root = ET.fromstring(r.text)

path = root.findall(".//path")

ws = []
for element in path:
    file = 's3:/'+ element.text
    print(file)
    ws.append(file)

```

    Enter your NIMH Data Archives username:ahmadus
    Enter your NIMH Data Archives password:········
    Enter package ID:108728
    s3://gpop/ndar_data/experiments/experiment_386/block_1/Block_Design_File/Sequence_GNG3and4_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_386/block_2/Block_Design_File/Sequence_GNG3and4_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_386/block_3/Block_Design_File/Sequence_GNG3and4_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_386/block_4/Block_Design_File/Sequence_GNG3and4_Block.txt
    s3://gpop/ndar_data/experiments/experiment_386/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_386/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_387/experiment_387.xml
    s3://gpop/ndar_data/experiments/experiment_387/block_1/Block_Design_File/Seq_File_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_387/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_387/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_388/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_388/experiment_388.xml
    s3://gpop/ndar_data/experiments/experiment_388/block_1/Block_Design_File/Seq_File_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_388/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_389/experiment_389.xml
    s3://gpop/ndar_data/experiments/experiment_389/block_1/Block_Design_File/Seq_File_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_389/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_389/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_515/experiment_515.xml
    s3://gpop/ndar_data/experiments/experiment_515/block_1/Block_Design_File/515_BlockDesignFiles.zip
    s3://gpop/ndar_data/experiments/experiment_515/block_1/Video_File/addblock_060414_jma.es
    s3://gpop/ndar_data/experiments/experiment_585/experiment_585.xml
    s3://gpop/ndar_data/experiments/experiment_585/block_1/Block_Design_File/CBT-Anx_EmoReg_description 10-19-2016.docx
    s3://gpop/ndar_data/experiments/experiment_585/block_2/Block_Design_File/CBT-Anx_EmoReg_description 10-19-2016.docx
    s3://gpop/ndar_data/experiments/experiment_585/block_3/Block_Design_File/CBT-Anx_EmoReg_description 10-19-2016.docx
    s3://gpop/ndar_data/experiments/experiment_747/experiment_747.xml
    s3://gpop/ndar_data/experiments/experiment_747/block_1/Block_Design_File/timing.xlsx
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/package_info.txt
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/image03.txt
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/cbcl01.txt
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/vinelandsurvey_200505.txt
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/guid_parent_child.txt
    s3://gpop/ndar_data/QueryPackages/PRODDB/Package_108728/concept_by_guid.txt
    s3://gpop/ndar_data/experiments/experiment_240/experiment_240.xml
    s3://gpop/ndar_data/experiments/experiment_240/block_1/Block_Design_File/P4_rewards_event_design.docx
    s3://gpop/ndar_data/experiments/experiment_241/block_1/Block_Design_File/P4_resting6min_Design.docx
    s3://gpop/ndar_data/experiments/experiment_240/Acquisition_Sequence_File/P4_Reward_Data_Acquisition.docx
    s3://gpop/ndar_data/experiments/experiment_240/ROI_File/ROI_File.docx
    s3://gpop/ndar_data/experiments/experiment_241/experiment_241.xml
    s3://gpop/ndar_data/QueryPackages/PRODDB/NDAR_README.pdf
    s3://gpop/ndar_data/experiments/experiment_381/block_1/Block_Design_File/Sequence_GNG1and2_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_380/Acquisition_Sequence_File/KIDMID_AcquisitionSequence.csv
    s3://gpop/ndar_data/experiments/experiment_380/ROI_File/KIDMID_ROIs.rtf
    s3://gpop/ndar_data/experiments/experiment_381/experiment_381.xml
    s3://gpop/ndar_data/experiments/experiment_381/block_2/Block_Design_File/Sequence_GNG1and2_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_381/block_3/Block_Design_File/Sequence_GNG1and2_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_381/block_4/Block_Design_File/Sequence_GNG1and2_Block.txt
    s3://gpop/ndar_data/experiments/experiment_381/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_381/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_382/experiment_382.xml
    s3://gpop/ndar_data/experiments/experiment_382/block_1/Block_Design_File/Sequence_GNG1and2_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_382/block_2/Block_Design_File/Sequence_GNG1and2_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_382/block_3/Block_Design_File/Sequence_GNG1and2_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_382/block_4/Block_Design_File/Sequence_GNG1and2_Block.txt
    s3://gpop/ndar_data/experiments/experiment_382/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_382/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_383/block_3/Block_Design_File/Sequence_GNG1and2_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_383/experiment_383.xml
    s3://gpop/ndar_data/experiments/experiment_383/block_1/Block_Design_File/Sequence_GNG1and2_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_383/block_2/Block_Design_File/Sequence_GNG1and2_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_383/block_4/Block_Design_File/Sequence_GNG1and2_Block.txt
    s3://gpop/ndar_data/experiments/experiment_383/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_383/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_384/experiment_384.xml
    s3://gpop/ndar_data/experiments/experiment_384/block_4/Block_Design_File/Sequence_GNG3and4_Block.txt
    s3://gpop/ndar_data/experiments/experiment_384/block_2/Block_Design_File/Sequence_GNG3and4_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_384/block_3/Block_Design_File/Sequence_GNG3and4_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_384/block_1/Block_Design_File/Sequence_GNG3and4_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_384/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_384/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_385/experiment_385.xml
    s3://gpop/ndar_data/experiments/experiment_385/block_1/Block_Design_File/Sequence_GNG3and4_GoFace.txt
    s3://gpop/ndar_data/experiments/experiment_385/block_2/Block_Design_File/Sequence_GNG3and4_NoGoFace.txt
    s3://gpop/ndar_data/experiments/experiment_385/block_3/Block_Design_File/Sequence_GNG3and4_ISI.txt
    s3://gpop/ndar_data/experiments/experiment_385/block_4/Block_Design_File/Sequence_GNG3and4_Block.txt
    s3://gpop/ndar_data/experiments/experiment_385/Acquisition_Sequence_File/Acq_Seq_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_385/ROI_File/ROI_Blank.txt
    s3://gpop/ndar_data/experiments/experiment_386/experiment_386.xml
    s3://gpop/ndar_data/experiments/experiment_241/ROI_File/ROI_File.docx
    s3://gpop/ndar_data/experiments/experiment_241/Acquisition_Sequence_File/P4_resting6min_Data_Acquisition.docx
    s3://gpop/ndar_data/experiments/experiment_242/experiment_242.xml
    s3://gpop/ndar_data/experiments/experiment_242/block_1/Block_Design_File/P4_faces_event_design.docx
    s3://gpop/ndar_data/experiments/experiment_242/Acquisition_Sequence_File/P4_faces_Data_Acquisition.docx
    s3://gpop/ndar_data/experiments/experiment_242/ROI_File/ROI_File.docx
    s3://gpop/ndar_data/experiments/experiment_364/experiment_364.xml
    s3://gpop/ndar_data/experiments/experiment_364/block_1/Block_Design_File/Biopoint_seq.txt
    s3://gpop/ndar_data/experiments/experiment_364/block_1/Video_File/ACE_BIOPOINT.zip
    s3://gpop/ndar_data/experiments/experiment_364/Acquisition_Sequence_File/ACQUI_SEQ.txt
    s3://gpop/ndar_data/experiments/experiment_364/ROI_File/ROI_Files.txt
    s3://gpop/ndar_data/experiments/experiment_366/experiment_366.xml
    s3://gpop/ndar_data/experiments/experiment_366/block_1/Block_Design_File/Faces_seq.txt
    s3://gpop/ndar_data/experiments/experiment_366/block_1/Video_File/ACE_FACES.zip
    s3://gpop/ndar_data/experiments/experiment_366/Acquisition_Sequence_File/ACQUI_SEQ.txt
    s3://gpop/ndar_data/experiments/experiment_366/ROI_File/ROI_Files.txt
    s3://gpop/ndar_data/experiments/experiment_367/experiment_367.xml
    s3://gpop/ndar_data/experiments/experiment_367/block_1/Block_Design_File/Sequence_file.txt
    s3://gpop/ndar_data/experiments/experiment_367/block_1/Video_File/ACE_LANGUAGE.zip
    s3://gpop/ndar_data/experiments/experiment_367/Acquisition_Sequence_File/ACQUI_SEQ.txt
    s3://gpop/ndar_data/experiments/experiment_367/ROI_File/ROI_Files.txt
    s3://gpop/ndar_data/experiments/experiment_368/experiment_368.xml
    s3://gpop/ndar_data/experiments/experiment_368/block_1/Block_Design_File/Resting_state_seq.txt
    s3://gpop/ndar_data/experiments/experiment_368/block_1/Video_File/ACE_RESTING_STATE.zip
    s3://gpop/ndar_data/experiments/experiment_368/Acquisition_Sequence_File/ACQUI_SEQ.txt
    s3://gpop/ndar_data/experiments/experiment_368/ROI_File/ROI_Files.txt
    s3://gpop/ndar_data/experiments/experiment_369/Acquisition_Sequence_File/ACQUI_SEQ.txt
    s3://gpop/ndar_data/experiments/experiment_369/experiment_369.xml
    s3://gpop/ndar_data/experiments/experiment_369/block_1/Block_Design_File/Reward_Seq.txt
    s3://gpop/ndar_data/experiments/experiment_369/block_1/Video_File/ACE_REWARD.zip
    s3://gpop/ndar_data/experiments/experiment_369/ROI_File/ROI_Files.txt
    s3://gpop/ndar_data/experiments/experiment_378/experiment_378.xml
    s3://gpop/ndar_data/experiments/experiment_378/block_1/Block_Design_File/Nonconscious_Faceview_Timing.csv
    s3://gpop/ndar_data/experiments/experiment_378/Acquisition_Sequence_File/Nonconscious_AcquisitionSequence.csv
    s3://gpop/ndar_data/experiments/experiment_378/ROI_File/Nonconscious_ROIs.rtf
    s3://gpop/ndar_data/experiments/experiment_379/experiment_379.xml
    s3://gpop/ndar_data/experiments/experiment_379/block_1/Block_Design_File/Conscious_Faceview_Timing.csv
    s3://gpop/ndar_data/experiments/experiment_379/Acquisition_Sequence_File/Conscious_AcquisitionSequence.csv
    s3://gpop/ndar_data/experiments/experiment_379/ROI_File/Conscious_ROIs.rtf
    s3://gpop/ndar_data/experiments/experiment_380/experiment_380.xml
    s3://gpop/ndar_data/experiments/experiment_380/block_1/Block_Design_File/ELS_T1_KIDMID_Scanner_Final_SB3.ebs2


<html>
    <h2>Using a miNDAR Package to Drive Exploration and Analysis</h2>
     <p>miNDAR is short for mini-NDAR, which is a remote database (Oracle) that you have control over and can push data to. This service requires authentication to ensure you are the miNDAR owner.</p>
    <ol><li>Connecting to the miNDAR containing the data you are interested in downloading</li>
    <li>Querying/Exploring data in the miNDAR</li>
    <li>Generating credentials for accessing s3 Objects</li>
    <li>Using credentials and s3 Object references from the miNDAR to retreive data</li></ol>
    
<h3>1. Connecting to the miNDAR containing the data you are interested in downloading</h3>
Once packaged, data can be pushed to a miNDAR in the form of where they will be availalbe as database tables and s3 object references. When data has finished loading into a miNDAR, you will receive an email with the connection information.
    <li>requires a Oracle client</li>
    <li>the following example uses Oracle Instant Client v12.2 and the python library cx_Oracle</li>
  
</html>


```python
import cx_Oracle
hostname = 'mindarvpc.cqahbwk3l1mb.us-east-1.rds.amazonaws.com'
port = 1521
sid = 'ORCL'

import getpass
username = input('Enter your miNDAR username:')#'username_package_id'
password = getpass.getpass('Enter your miNDAR password:')
dsnStr = cx_Oracle.makedsn(hostname, port, sid )
db = cx_Oracle.connect(user=username, password=password, dsn=dsnStr)

```

    Enter your miNDAR username:ahmadus_108728
    Enter your miNDAR password:········


<html>
    
<h3>2. Querying/Exploring Data in the miNDAR</h3>
After negotiating a successful connection we can query the miNDAR directly using SQL. We can retreive these results and store them as objects in R, Python, and many other programming languages.
Here we will query the table CONCEPT_BY_GUID, which is available in all miNDAR packages.
<li>in this example we store the results in a pandas dataframe (requries pandas)</li>
</html>


```python
#here we can retrieve the s3 URLs for image_file and data_file assoicated with each subject from the image03 table. 
#there is also an S3_LINKS table that lists all the s3 URLs available. 

import pandas as pd
import pandas.io.sql as psql

query = """SELECT subjectkey, image_file, data_file2
            FROM IMAGE03
            WHERE data_file2 IS NOT NULL"""
            
c = db.cursor()
c.execute(query)
data_files = pd.DataFrame(c.fetchall())
data_files.columns = [rec[0] for rec in c.description]

print(data_files)

miNDAR = []
for file in data_files['IMAGE_FILE']:
    miNDAR.append(file)

```

               SUBJECTKEY                                         IMAGE_FILE  \
    0    NDAR_INVWY997MTT  s3://NDAR_Central_2/submission_11013/019000001...   
    1    NDAR_INVWY997MTT  s3://NDAR_Central_2/submission_11013/019000001...   
    2    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    3    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    4    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    5    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    6    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    7    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    8    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    9    NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    10   NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    11   NDAR_INVVR979JTD  s3://NDAR_Central_2/submission_11013/019000001...   
    12   NDAR_INVVJ578CMG  s3://NDAR_Central_2/submission_11013/019100001...   
    13   NDAR_INVVJ578CMG  s3://NDAR_Central_2/submission_11013/019100001...   
    14   NDAR_INVVJ578CMG  s3://NDAR_Central_2/submission_11013/019100001...   
    15   NDAR_INVVJ578CMG  s3://NDAR_Central_2/submission_11013/019100001...   
    16   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    17   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    18   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    19   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    20   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    21   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    22   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    23   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    24   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    25   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    26   NDAR_INVKV252NFR  s3://NDAR_Central_2/submission_11013/000300001...   
    27   NDAR_INVWT045MFH  s3://NDAR_Central_2/submission_11013/019000001...   
    28   NDAR_INVWT045MFH  s3://NDAR_Central_2/submission_11013/019000001...   
    29   NDAR_INVWT045MFH  s3://NDAR_Central_2/submission_11013/019000001...   
    ..                ...                                                ...   
    347      NDARXZ339MZR  s3://NDAR_Central_3/submission_13674/NDARXZ339...   
    348      NDARXZ339MZR  s3://NDAR_Central_3/submission_13674/NDARXZ339...   
    349      NDARTZ403TKU  s3://NDAR_Central_3/submission_13674/NDARTZ403...   
    350      NDARTZ403TKU  s3://NDAR_Central_3/submission_13674/NDARTZ403...   
    351      NDARTZ403TKU  s3://NDAR_Central_3/submission_13674/NDARTZ403...   
    352      NDARTZ403TKU  s3://NDAR_Central_3/submission_13674/NDARTZ403...   
    353      NDARCN383ZEE  s3://NDAR_Central_2/submission_13629/NDARCN383...   
    354      NDARKT871JV1  s3://NDAR_Central_2/submission_13629/NDARKT871...   
    355      NDARCY843HKN  s3://NDAR_Central_2/submission_13629/NDARCY843...   
    356      NDARFU868CVF  s3://NDAR_Central_2/submission_13629/NDARFU868...   
    357      NDARYM862JK7  s3://NDAR_Central_2/submission_13629/NDARYM862...   
    358      NDARHK897GZX  s3://NDAR_Central_2/submission_13629/NDARHK897...   
    359      NDARFX414AHK  s3://NDAR_Central_2/submission_13629/NDARFX414...   
    360      NDARHU658FF2  s3://NDAR_Central_2/submission_13629/NDARHU658...   
    361      NDAREW988FK7  s3://NDAR_Central_2/submission_13629/NDAREW988...   
    362      NDARHX274AFB  s3://NDAR_Central_2/submission_13629/NDARHX274...   
    363      NDARKC776CY3  s3://NDAR_Central_2/submission_13629/NDARKC776...   
    364      NDARMN436JP7  s3://NDAR_Central_2/submission_13629/NDARMN436...   
    365      NDARFA755YRA  s3://NDAR_Central_2/submission_13629/NDARFA755...   
    366      NDARJZ207PA0  s3://NDAR_Central_2/submission_13629/NDARJZ207...   
    367      NDARDG846PFF  s3://NDAR_Central_2/submission_13629/NDARDG846...   
    368      NDARNX466MBV  s3://NDAR_Central_2/submission_13629/NDARNX466...   
    369      NDARDR403NPK  s3://NDAR_Central_2/submission_13629/NDARDR403...   
    370      NDARCN383ZEE  s3://NDAR_Central_2/submission_13629/NDARCN383...   
    371      NDARKT871JV1  s3://NDAR_Central_2/submission_13629/NDARKT871...   
    372      NDARCY843HKN  s3://NDAR_Central_2/submission_13629/NDARCY843...   
    373      NDARFU868CVF  s3://NDAR_Central_2/submission_13629/NDARFU868...   
    374      NDARJC516JZF  s3://NDAR_Central_2/submission_13629/NDARJC516...   
    375      NDARJC516JZF  s3://NDAR_Central_2/submission_13629/NDARJC516...   
    376      NDARHK897GZX  s3://NDAR_Central_2/submission_13629/NDARHK897...   
    
                                                DATA_FILE2  
    0    s3://NDAR_Central_2/submission_11013/019000001...  
    1    s3://NDAR_Central_2/submission_11013/019000001...  
    2    s3://NDAR_Central_2/submission_11013/019000001...  
    3    s3://NDAR_Central_2/submission_11013/019000001...  
    4    s3://NDAR_Central_2/submission_11013/019000001...  
    5    s3://NDAR_Central_2/submission_11013/019000001...  
    6    s3://NDAR_Central_2/submission_11013/019000001...  
    7    s3://NDAR_Central_2/submission_11013/019000001...  
    8    s3://NDAR_Central_2/submission_11013/019000001...  
    9    s3://NDAR_Central_2/submission_11013/019000001...  
    10   s3://NDAR_Central_2/submission_11013/019000001...  
    11   s3://NDAR_Central_2/submission_11013/019000001...  
    12   s3://NDAR_Central_2/submission_11013/019100001...  
    13   s3://NDAR_Central_2/submission_11013/019100001...  
    14   s3://NDAR_Central_2/submission_11013/019100001...  
    15   s3://NDAR_Central_2/submission_11013/019100001...  
    16   s3://NDAR_Central_2/submission_11013/000300001...  
    17   s3://NDAR_Central_2/submission_11013/000300001...  
    18   s3://NDAR_Central_2/submission_11013/000300001...  
    19   s3://NDAR_Central_2/submission_11013/000300001...  
    20   s3://NDAR_Central_2/submission_11013/000300001...  
    21   s3://NDAR_Central_2/submission_11013/000300001...  
    22   s3://NDAR_Central_2/submission_11013/000300001...  
    23   s3://NDAR_Central_2/submission_11013/000300001...  
    24   s3://NDAR_Central_2/submission_11013/000300001...  
    25   s3://NDAR_Central_2/submission_11013/000300001...  
    26   s3://NDAR_Central_2/submission_11013/000300001...  
    27   s3://NDAR_Central_2/submission_11013/019000001...  
    28   s3://NDAR_Central_2/submission_11013/019000001...  
    29   s3://NDAR_Central_2/submission_11013/019000001...  
    ..                                                 ...  
    347  s3://NDAR_Central_3/submission_13674/NDARXZ339...  
    348  s3://NDAR_Central_3/submission_13674/NDARXZ339...  
    349  s3://NDAR_Central_3/submission_13674/NDARTZ403...  
    350  s3://NDAR_Central_3/submission_13674/NDARTZ403...  
    351  s3://NDAR_Central_3/submission_13674/NDARTZ403...  
    352  s3://NDAR_Central_3/submission_13674/NDARTZ403...  
    353  s3://NDAR_Central_2/submission_13629/NDARCN383...  
    354  s3://NDAR_Central_2/submission_13629/NDARKT871...  
    355  s3://NDAR_Central_2/submission_13629/NDARCY843...  
    356  s3://NDAR_Central_2/submission_13629/NDARFU868...  
    357  s3://NDAR_Central_2/submission_13629/NDARYM862...  
    358  s3://NDAR_Central_2/submission_13629/NDARHK897...  
    359  s3://NDAR_Central_2/submission_13629/NDARFX414...  
    360  s3://NDAR_Central_2/submission_13629/NDARHU658...  
    361  s3://NDAR_Central_2/submission_13629/NDAREW988...  
    362  s3://NDAR_Central_2/submission_13629/NDARHX274...  
    363  s3://NDAR_Central_2/submission_13629/NDARKC776...  
    364  s3://NDAR_Central_2/submission_13629/NDARMN436...  
    365  s3://NDAR_Central_2/submission_13629/NDARFA755...  
    366  s3://NDAR_Central_2/submission_13629/NDARJZ207...  
    367  s3://NDAR_Central_2/submission_13629/NDARDG846...  
    368  s3://NDAR_Central_2/submission_13629/NDARNX466...  
    369  s3://NDAR_Central_2/submission_13629/NDARDR403...  
    370  s3://NDAR_Central_2/submission_13629/NDARCN383...  
    371  s3://NDAR_Central_2/submission_13629/NDARKT871...  
    372  s3://NDAR_Central_2/submission_13629/NDARCY843...  
    373  s3://NDAR_Central_2/submission_13629/NDARFU868...  
    374  s3://NDAR_Central_2/submission_13629/NDARJC516...  
    375  s3://NDAR_Central_2/submission_13629/NDARJC516...  
    376  s3://NDAR_Central_2/submission_13629/NDARHK897...  
    
    [377 rows x 3 columns]


<html>
    
    <h3> 3. Generating credentials for accessing s3 Objects</h3>
    
Here we will generate credentials using our NIMH Data Archives username and password, which will allow us to authenticate and retreive data from AWS s3 Object storage for any shared objects.

<h4>There are a few ways you can generate tokens to access AWS s3 object storage</h4>
<li>You can generate credentails using the Download Manager GUI</li>
<li>We will use a python package for generating tokens, which is available on our GitHub.</li>



<h2>Generate FederatedToken</h2>
<ol><li>pip install git+https://github.com/NDAR/nda_aws_token_generator.git#egg=nda-aws-token-generator&subdirectory=python</li>
    <li>cd ~/nda_aws_token_generator/python/</li>
    <li>sudo python setup.py install</li></ol>



    </html>


```python
from getpass import getpass

url = 'https://ndar.nih.gov/DataManager/dataManager'
username = input('Enter your NIMH Data Archives username:')
password = getpass('Enter your NIMH Data Archives password:')

from nda_aws_token_generator import *
generator = NDATokenGenerator(url)
token = generator.generate_token(username, password)

print('aws_access_key_id=%s\n'
      'aws_secret_access_key=%s\n'
      'security_token=%s\n'
      'expiration=%s\n' 
      %(token.access_key,
        token.secret_key,
        token.session,
        token.expiration)
      )
```

    Enter your NIMH Data Archives username:ahmadus
    Enter your NIMH Data Archives password:········
    aws_access_key_id=ASIAIHO3YY6GIEHOVCOQ
    aws_secret_access_key=joJkGvuw4/h38SwsPANbA9AUrW9vlRsZm/G/Iq3v
    security_token=FQoDYXdzEN3//////////wEaDAZOHF25l8mN3sZWmCLUAbbyBzPbB/hrKK20w9wSt6JbGCc0pqu4/I+TatqQtkmEs1FP2DmrYFPDVAe99PYKOL2lqa9qA+rDPHk2PkLVzBDkhsBc001dRQsHjBrbmu8hqJrGIVB5RGqML9K/41SLqpHLnXEzSxGICG/V+S/v37yaykXSq+QWvOn/kXcOOSJhtWiI5zYMrVDQkW9VpySrvdwp9IorMJKCrtgt2CHlTqEExWAk3gyEg/VDhZlFnkKeHZl2Dm9fY9P1ivpWPnJCLTVhBGpPEtff3K5BB7WdbNpaL8w5KKX56tEF
    expiration=2017-12-21T02:40:21-05:00
    


<html>
    <h3>4. Using credentials and s3 Object references from the miNDAR to retreive data</h3>

Here we will combine our s3 credentials and the data we retrieved from the miNDAR, using the image_file and  data_file2 column that has our s3 Object references to retreive some Variant Call data about a subject.
    <li>We will use boto to interface with s3 objects</li>


```python
# Pull image out of S3

file = input("Enter S3 URL:")
#s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz

import boto.s3.connection
from urllib.parse import urlparse

cf = boto.s3.connection.OrdinaryCallingFormat()
conn = boto.connect_s3( token.access_key,
                        token.secret_key,
                        security_token=token.session,
                        calling_format=cf)

bucket = urlparse(file).netloc
key = urlparse(file).path
bucket_object = conn.get_bucket(bucket)
s3_object = boto.s3.key.Key(bucket_object)
s3_object.key = key
name = key.split('/')
name = name[-1]
byte_data = s3_object.get_contents_to_filename(name) #edit this file name to actually match s3
```

    Enter S3 URL:s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz


<html>
<p>The downloaded file can now be viewed and analyzed.  <b>It should be noted that the boto package provides functionality to read the object into memory as a 'string', which could be passed to other functions, and boto also supports streaming the content.</b></p>
</html>


```python
#lists = [dm, ws, miNDAR]
#will save only first five files in the list
count = 1
for file in dm:
    bucket = urlparse(file).netloc
    key = urlparse(file).path
    bucket_object = conn.get_bucket(bucket)
    s3_object = boto.s3.key.Key(bucket_object)
    s3_object.key = key
    name = key.split('/')
    name = name[-1]
    byte_data = s3_object.get_contents_to_filename(name) #edit this file name to actually match s3
    print(name)
    count += 1
    if count > 5:
        break

```

    NDARAB369MB6_image03_1373498869756.zip
    NDARAB369MB6_image03_1373498869756.jpg
    NDARAB369MB6_image03_1373497889885.zip
    NDARAB369MB6_image03_1373497889885.jpg
    NDARAB369MB6_image03_1373646986954.zip


<html>
<h2>New Functionality</h2>
<ul>
<li>Scratch Space provided</li>
<li>Computational Credits</li>
<li>Data Submission via Web Services</li>
</ul>
</html>


<html>
<div>
    <h3>Available APIs <a href="https://data-archive.nimh.nih.gov/API">https://data-archive.nimh.nih.gov/API</a></h3>
    <ul>
    
    <li>Data Dictionary <a href="https://ndar.nih.gov/swagger">https://ndar.nih.gov/api/datadictionary</a></li>
        
    <li>Search <a href="https://ndar.nih.gov/api/search">https://ndar.nih.gov/api/search</a></li>
    
    <li>Collection <a href="https://ndar.nih.gov/api/collection">https://ndar.nih.gov/api/collection</a></li>
    
    <li>GUID <a href="https://ndar.nih.gov/api/guid">https://ndar.nih.gov/api/guid</a></li>
    
    <li>Experiment <a href="https://ndar.nih.gov/swagger">https://ndar.nih.gov/api/experiment</a></li>

    <li>miNDAR <a href="https://ndar.nih.gov/api/mindar">https://ndar.nih.gov/api/mindar</a></li>
    
    
    </ul>
    
    </div>
 </html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>GUID Webservice</h2>
        <p>Provides the capability to programmatically access all submitted accross projects data for a specifc subject.</p>
        <p>This service requires authentication and will only return data that is accessible to your user, based on your privleges and permisisons on the data.</p>
    </div>
    <p>
    <a href="https://ndar.nih.gov/api/guid">Swagger User Interface</a>
    </p>
</html>


```python
import requests
import json
from getpass import getpass
#NDAR_INVRT663MBL
#NDAR_INVEP756TR3
#NDARBV344JLX

username = input("What is your NDA username:")
password = getpass("What is your NDA password:")
guid = input("What GUID would you like to access data from:")
#r = requests.get("https://ndar.nih.gov/api/guid/{}/data?short_name=image03".format(guid), 
#                 auth=requests.auth.HTTPBasicAuth(username, password),
#                 headers={'Accept': 'application/json'})

r = requests.get("https://stage.nimhda.org/api/guid/{}/data?short_name=image03".format(guid), 
                 auth=requests.auth.HTTPBasicAuth(username, password),
                 headers={'Accept': 'application/json'})

guid_data = json.loads(r.text)
print(guid_data)
```


```python
# Extract experiment IDs from response

experiments = []
ages = []
for age in guid_data['age']:
    age_value = age['value']
    for row in age['dataStructureRow']:
        for element in row['dataElement']:
            if element['name']=='EXPERIMENT_ID':
                if element['value'] not in experiments:
                    experiments.append(element['value'])

for experiment in experiments:
    print('experiment: {}'.format(experiment))
```


```python
# In previous 2 slides, have identified some fMRI, EEG, or Eye Tracking data; show how to retreive experimental details.

query = input("Enter your experiment ID:")
r = requests.get("https://ndar.nih.gov/api/experiment/{}".format(query),
                 headers={'Accept':'application/json'})

experiment = json.loads(r.text)
print(experiment)
```


```python
# Pull out image files from response
image_files = []
ages = []
for age in guid_data['age']:
    age_value = age['value']
    for row in age['dataStructureRow']:
        for link in row['links']['link']:
            if link['rel']=='data_file':
                image_files.append(link['href'])
                ages.append(age_value)
guid_list = []
for i,image in enumerate(image_files):
    print("age:{}, url:{}".format(ages[i],image))
    guid_list.append(image)
    
```

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Search Webservice</h2>
        <p>Provides the capability for programmatic search across all NDA sites (NDAR, pediatricMRI, ABCD, Clinical Trials, Human Connectome Project, etc.) enabling users to identify projects with data of potential interest.</p>
        <p>Search content includes experimental information, project descriptions, investigators, grant numbers, page-content, and all data elements that make up the 1000s of measures defined in the data dictionary.</p>
    </div>
    
    <p>
        <a href="https://ndar.nih.gov/api/search">Swagger User Interface</a>
    </p>
</html>

<html>
<div>
<h2>Full Search</h2>
<p>Search resource that allows for querying a word or phrase and identifying matching content, studies, collections, experiments, and data elements.</p>
</div>
<h2>Data Element Search</h2>
<p>Search resource that allows for specifying attributes of a data element and querying the entire dictionary for matching elements.</p>
<div>
<table style="float:left; margin-right:10px;">
<thead><tr><td>Attribute</td><td>Type</td></tr></thead>
<tbody>
  <tr><td>name</td><td>string</td></tr>
  <tr><td>description</td><td>string</td></tr>
  <tr><td>valueRanges</td><td>string</td></tr>
  <tr><td>notes</td><td>string</td></tr>
  <tr><td>type</td><td>string</td></tr>
  <tr><td>allQuery</td><td>string</td></tr>
</tbody>
</table>
</div>
</html>


```python
# Data Element Full Search

import requests
import json

query_phrase = input("Enter a description phrase:") #example: ABCD, depression, autism

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=10', 
                  headers={'Accept':'application/json'}, data= query_phrase)

search_results = json.loads(r.text)

data_elements = search_results['datadict']
print ('Total data structures:', data_elements['total'])
print()

for i in data_elements['results']: #filter the data structures
    if i['_score'] > 0.33:
        if query_phrase.lower() in i['description'].lower():
            print ('Name:', i['name'])
            print ('id:', i['id'])
            print ('Notes:', i['notes'])
            print ('Description:', i['description'])
            print ('Score:', i['_score'])
            print ('Data Structures:')
            for k in i['dataStructures']:
                print(k)
            print ('Total Data Structures:', i['total_data_structures'])
            print()

```


```python
# Data Element Search

description = input("Enter a description to query:")
query = {'description': description}
r = requests.post("https://stage.nimhda.org/api/search/nda_sw_removal/dataElementSearch?size=20", 
                  data=json.dumps(query),
                  headers={'content-type':'application/json'})
element_results = json.loads(r.text)
for result in element_results['dataElements']: 
    print("score:{}\nname:{}\ndescription:{}\n".format(result['score'], result['name'], result['description']))
```


```python
# Here is a programmatic example searching by collection
import requests
import json


class collectionLink():

    def __init__(self, title, id):
            self.id = id
            self.title = title
            self._repr_html_()

    def _repr_html_(self):
        collection_link = 'https://ndar.nih.gov/edit_collection.html?id={}'.format(self.id)
        html = ['<a href="{}">{}</a>'.format(collection_link, self.title)]
        return ''.join(html)

    
query = input("Enter your query phrase:")
r = requests.post("https://ndar.nih.gov/api/search/nda_sw_removal/collection/full", query)
collections = json.loads(r.text)
print("\n")
for result in collections['collection']['results']:
    display(collectionLink(result['title'],result['id'])) 
```

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Data Dictionary Webservice</h2>
        <p>Provides the capability for programmatic interrogation of all available datastructures/measures, by name, type, source, and category.  The service also provides element-level detail.</p>
        <p>Additionally, a history of changes can be retreived for both data sturcture and data elements.</p>
    </div>
    <p>
        <a href="https://ndar.nih.gov/swagger">Swagger User Interface</a>
    </p>
</html>


```python
# Progromatically retrieve data from the dictionary service
# Example data structure shortname: image03

import requests
import json
shortname = input('Enter a Data Structure shortname:')
r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/datastructure/{}'
                 .format(shortname),
                  headers={'Accept':'application/json'})
structure = json.loads(r.text)

# Get Data Structure change history

r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/datastructure/{}/changes'
                 .format(shortname),
                  headers={'Accept':'application/json'})

changes = json.loads(r.text)
```


```python
# Show data structure elements that are required, or potentially required (conditional)

for element in structure['dataElements']:
    if element['required'] in ['Required','Conditional']:
        print('elementInfo: {}\n'.format(element))
```


```python
# Show element name for all data elements with type as 'file'

for element in structure['dataElements']:
    if element['type'] == 'File':
        print('elementName: {}'.format(element['name']))
```


```python
# Get data element info and changes
from IPython.display import display

class changeHistoryTable():
    
    def __init__(self, list):
        self.list = list
        self.headers = ['id','changeDescription','changedDate','elementName','newValue','oldValue','shortName']
        self._repr_html_()
    
    def _repr_html_(self):

        html = ["<table width=100%>"]
        html.append("<thead><tr>")
        for header in self.headers:
            html.append("<td>{}</td>".format(header))
        html.append("</tr></thead><tbody>")      

        for row in self.list:
            html.append("<tr>")
            for header in self.headers:
                html.append("<td>{}</td>".format(row[header]))
            html.append("</tr>")
        html.append("</tbody></table>")
        return ''.join(html)

change_list = []
        
for element in structure['dataElements']: #search data elements in a data structure
    if element['type'] == 'File':
        r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/dataelement/{}' 
                 .format(element['name']),
                  headers={'Accept':'application/json'})
        elementInfo = json.loads(r.text) #information about the data element
        
        r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/dataelement/{}/changes'
                .format(element['name']),
                headers={'Accept':'application/json'})
        changes = json.loads(r.text) #information about the data element changes
        try:
            change_list.extend(changes['list'])
        except KeyError:
            print('No changes for elementName {}'.format(element['name']))

display(changeHistoryTable(change_list))
```


```python
# Data Element Data Structure Search
# Returns a list of data structures for data element alphabetically
# Example data elements: gender, subjectkey

dataelement = input("Enter a data element name:")

r = requests.get('https://ndar.nih.gov/api/search/nda_sw_removal/dataElementDataStructures?name={}'.format(dataelement), 
                  headers={'Accept':'application/json'})

element = json.loads(r.text)

for data in element['dataElements']:
    for structure in data['dataStructures']:
        print("id:{}\ncategory:{}\nshortName:{}\nsubjectCount:{}\n".format(structure['id'], structure['category'], structure['shortName'], structure['subjectCount']))
```
