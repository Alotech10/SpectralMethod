"""
   Script to test the algorithm presented on the paper
   ''A new spectral method for Latent Variable Models''

   Here the user can generate random synthetic texts
   and test the accuracy of the proposed algorithm.
   """


#######################################################################
## Imports
#######################################################################
import RandomGenerator as rand
import SpectralMethod as sm
import numpy as np

#######################################################################
## Set here the model parameters:
#######################################################################
N = 1000                    #The number of documents
n = 6                       #The size of the vocabulary
k = 3                       #The number of topics
c = 3000                    #The number of words per document
TestSingleTopic = False     #Set to true to test the single topic model, to false to test LDA

if TestSingleTopic:
    X,M,omega = rand.generate_sample_SingleTopic(N,n,k,c)
    M1,M2,M3 = sm.RetrieveTensorsST(X)
    M_tilde,omega_tilde = sm.learn_LVM_Core(M1,M2,M3,k)
    print(np.linalg.norm(M_tilde.dot(np.diag(omega_tilde)).dot(M_tilde.T) - M.dot(np.diag(omega)).dot(M.T) ))
else:
    X, M, Alpha = rand.generate_sample_LDA(N, n, k, c)
    Alpha0 = np.sum(Alpha)
    M1a,M2a,M3a = sm.RetrieveTensorsLDA(X, Alpha0)
    M_tilde,Alpha_tilde = sm.learn_LVM_Core_LDA(M1a, M2a, M3a, Alpha0, k)

