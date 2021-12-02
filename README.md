# agn-psr-nn-classification

![map_dnn](https://user-images.githubusercontent.com/37272943/101777807-48eeb700-3af3-11eb-9eb2-e12479c2a7e6.png)

This repository contains neural network predictions for the class of unassociated gamma-ray sources in Fermi-LAT 4FGL-DR2 catalog.
In what follows you find the list of candidates obtained for:

1-the classification of unassociated sources into Active Galactic Nuclei, Pulsars, Young Pulsars and Millisecond pulsars (folder DNN_RNN/)

2-the classification of blazars of uncertain type into Flat Spectrum Radio Quasars and BL Lacertae objects (folder BNN/)

as obtained in the following two papers:

1-'Classification of Fermi-LAT sources with deep learning using energy and time spectra' by Thorben Finke, Michael Kraemer, and Silvia Manconi

arXiv:2012.05251, Mon.Not.Roy.Astron.Soc. 507 (2021) 3, 4061-4073 

2-'Classification of Fermi-LAT blazars with Bayesian neural networks' by Anja Butter, Thorben Finke, Felicitas Keil, Michael Kraemer, and Silvia Manconi

arXiv:2112.XXXX

The list of sources are provided as .npz files, together with a small script to read them. 

Please refer to the corresponding paper for more details on the machine learning techniques used to obtain the
list of candidates, the estimated accuracy of each selection and the characteristics of the candidate sources in each class.  

For questions and doubts, please do not hesitate to write us!

manconi@physik.rwth-aachen.de
