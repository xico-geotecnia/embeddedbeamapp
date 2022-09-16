# englib- an [interactive](https://web.microsoftstream.com/video/cbaf7584-4845-473b-8817-419eccfde300?st=839&et=850) library for [project calculations](https://web.microsoftstream.com/video/87a25a46-21a8-4ad4-b7e3-fa17f897a768?st=2237&et=2367).




<IMG SRC='docs/englib_logo_large.PNG' ALIGN='left' HSPACE='20'/>
englib (engineer's library) is a package which contains clauses, equations, charts, tables and figures from the standards and guidance which COWI engineers rely on in their work. This includes, but is not restricted to, Eurocodes and other Euronorms, Blue Book section properties, design guides and other design standards from around the world. The content is functional- for example, equations are displayed and also executed, charts are interpolated and that interpolation shown on a reproduction of the chart, entries are pulled out of tables. The standard and version that the content came from is signposted clearly. The package is set up in a way that makes it easy to modify functionality over the entire library- for example, changing the way clauses are displayed. It is also easy to add new content (e.g. code clauses) in a distributed way as more users deploy it on more projects. Englib provides a key missing link in project delivery using a digital workflow. It ties the workflow explicitly to the necessary standards which we are obliged to comply with.
<br>
<br>



## try it out



### tutorials



englib/examples/englib_tutorials contains tutorials about how to use englib (englib_user_tutorial.py), how to add more content to it (englib_adder_tutorial.py) and how to QA content created by others (englib_curator_tutorial.py).
  
link to [bitesize tutorials](https://web.microsoftstream.com/channel/69c7ac64-9038-4357-b9e1-3013ff5947e0).  



### cribsheets



englib/examples/cribsheets contains cribsheets- worked examples of engineering calculations.
The cribsheets are intended to familiarise users with how to use englib aswell as provide a template for common calculations that engineers undertake.
The cribsheets are best run in jupyter notebook.



| | |
| - | - |
| *Buckling.py*: an axial buckling calculation. | ![content_example](docs/content_equation.PNG) |
| *shear_lag.py*: a shear lag modification calculation. | ![content_example](docs/shear_lag.PNG) |
| *fillet_weld.py*: a fillet welded joint verfication. | ![content_example](docs/fillet.PNG) |




## Install



#### install to get started and for the englib hackathon



to get cracking we now recommend the following [instructions](http://git.cowiportal.com/mwsy/englib_hackathon#installation)




#### To install an editable version of englib



To install englib only



* clone this repository (eg using GitHub Desktop) <br>
* run the following with the working directory set to where you have put the englib folder. <br>



```conda
pip install -e englib
```




#### I have not got the COWI UK Environment Installed



NOTE: this is the old way... no longer recommended



Follow [these steps](http://git.cowiportal.com/Team-COWI_UK/COWICommon/#setup-for-using-cowi-uk-packages) <br>



#### I already have the COWI UK Environment Installed



NOTE: this is the old way... no longer recommended



* make sure you have the most up to date COWI UK environment: <br>
    * switch to the master branch of COWI Common and pull origin
    * run the following in conda
    ```conda
    cd c:\cowi uk tools\cowicommon
    conda env update -f cowi_uk_env.yml  --prune
    ```
* clone this repository (eg using GitHub Desktop)- make sure you save it in your COWI UK tools folder! <br>
* run the following in conda (under COWI UK env)



```conda
cd c:\COWI UK tools
pip install -e englib
```



#### install jupyter notebook extensions



The nbextensions toolbar is useful to use with jupyter notebooks - these allow you to use table of contents 2 (with handy navigation pane) and hide input cells- which allows you to hide the code cells.



to install run following in conda



```conda
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```



After running these commands, the nbextensions tab will appear on your jupyter notebook start up window, where you can select the extensions that you wish to use



## QA Process



Architectually, ```englib``` can be split into two distinct areas
|  |Functionality | Content |
| - |  - | - |
| description | Feature classes which define behavior | Instances of feature classes |
| example | ```Equation``` | ```en_1993_1_1.equation_6_49``` which is an instance of ```Equation``` |
| location | ```englib.py``` | content files within folders eg ```euronorms/en_1993_1_1.py```|
| programming ability required for development | moderate | low |
| risk of changes causing breaking | moderate | low, because instances are fairly decoupled |
| QA protocol | [COWI Programming Governance](http://git.cowiportal.com/webApp/Tool-Git/Programming_Governance/) | [COWI Programming Governance](http://git.cowiportal.com/webApp/Tool-Git/Programming_Governance/), with a specific process set out below |



### content



![qa_process_flow](docs/qa_process_flow.png)



The library is envisioned to grow as users on projects add content that doesn't already exist. <br>
A new item can be added to the library through the [following stages](https://web.microsoftstream.com/video/fe6e5cc7-b49b-404d-9b48-d2c9a69ae29b?st=62&et=278).
1. Initially, the user works off the current ```englib``` release on the ```master``` branch
2. If the user wants to use an item that doesn't yet exist, they switch to ```develop``` branch
3. The user checks if the item exists on ```develop```
    * If it does exist, it will be have ```approved``` attibute set to ```False``` and the user should check with a curator directly to ascertain sutiability for their application.
4. If it does not, the user creates a new branch based off ```develop``` , adds the feature (making sure to set ```approved``` equal to ```False```) and issues a pull request to merge to ```develop``` . They assingn englib_curators as reviewer of the pull request.
5. The request is immediately subjected to automated unittests, checking that the new feature can accept required inputs and that it does not break anything else. The englib curator will check these pass, and conduct one two quick additional checks. They will then approve the request expediently.
6. Assuming approval, the item is merged to ```develop``` and the user can then work on the develop branch, the item of content will display a [warning message](https://web.microsoftstream.com/video/fe6e5cc7-b49b-404d-9b48-d2c9a69ae29b?st=899&et=905), ensuring that users know it is unchecked.
7. To remove the warning message, an [independent engineer must conduct a quality check](https://web.microsoftstream.com/video/6d9f66a0-b424-4d39-9533-944126a6ca81?st=48) according to the  [mandatory QA procedure](http://git.cowiportal.com/Team-COWI_UK/englib/src/branch/master#mandatory-qa-procedure)
8. When the time comes for the next release of ```englib``` the now approved new item of content will be merged into master and included in the new release, along with all other qa'd content added since the last release.




## mandatory QA procedure



* discuss status of new content with creator
* determine if content is within curator's area of competance, if not secure additional consultation from subject matter expert
* run unittests and check appropriate unittests have been written for the new content
* check
    * close check against the sources material- the latest version must be extracted eg from IHS
    * references are up to date
    * nomenclature is correct
    * englib conventions are followed
    * contextual nuances
* if new content extends or supersedes the content in the standard (ie it represents additional cowi expertise) then seek confirmation from creator that the new material is appropriately QA'd itself.



## englib curators
The current curators are
| | | Field |
| - | -| - |
|MWSY | Matthew Sheasby | |
|DNGR | Daniel Green | Structural |
|JKHC | Jack Hancock | Geotechnical |




## process for keeping content up to date



* current curators must gather all [IHS notifications](https://cowi.sharepoint.com/sites/B060776/Shared%20Documents/Codes%20and%20Standards/IHS%20Markit%20Standards%20Login%20Microsite/COWI-v18/London.aspx) that occur over a between release  
    * for corrections and minor revisions make commits to develop with changes noted as a markdown comment in the content files
    * for brand new versions or where the organisation of the standard changes a new content files is created and the old version renamed with a suffix denoting its version. Those wishing to run old standards can either use an old release or change the reference in import
eg
```python
from englib.euronorms import en_1993_1_1
```
becomes
```python
from englib.euronorms import en_1993_1_1_2005_A1 as en_1993_1_1
```



## procedure for new release



* mandatory QA process followed for all new content
* create a release branch off develop
* create pull request from release branch to master
* add release number to new content in content log
* remove un-qa'd content in one commit (from content log and unittests too)
* version number in __version__.py upped with the next [date base release](https://www.python.org/dev/peps/pep-0440/#id26)
* adjust changelog
* approve request
* new release tag added
* merge changes from master back to develop (PR not required)
* develop release tag in __version__.py given YYYY.a.dev so that this appears if develop branch used
* revert un-qa'd content removal commit
* prepare changelog
    
