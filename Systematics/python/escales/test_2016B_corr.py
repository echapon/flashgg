import FWCore.ParameterSet.Config as cms

photonSmearBins = cms.PSet(
    variables = cms.vstring("abs(superCluster.eta)","r9"),
    bins = cms.VPSet(
            # smearings for rereco 2015, photons,
            # see Fasanella et al., ECAL DPG 17/12/2015, https://indico.cern.ch/event/402608/contribution/1/attachments/1206871/1758949/DPG_reReco_corrections.pdf
        cms.PSet(lowBounds=cms.vdouble(0.000,-999.000), upBounds=cms.vdouble(1.000,0.940),   values=cms.vdouble(0.00993), uncertainties=cms.vdouble(0.0004)),
        cms.PSet(lowBounds=cms.vdouble(0.000,0.940),    upBounds=cms.vdouble(1.000,999.000), values=cms.vdouble(0.00899), uncertainties=cms.vdouble(0.0004)),
        cms.PSet(lowBounds=cms.vdouble(1.000,-999.000), upBounds=cms.vdouble(1.500,0.940),   values=cms.vdouble(0.0152), uncertainties=cms.vdouble(0.0006)),
        cms.PSet(lowBounds=cms.vdouble(1.000,0.940),    upBounds=cms.vdouble(1.500,999.000), values=cms.vdouble(0.0136), uncertainties=cms.vdouble(0.0019)),
        cms.PSet(lowBounds=cms.vdouble(1.500,-999.000), upBounds=cms.vdouble(2.000,0.940),   values=cms.vdouble(0.0158), uncertainties=cms.vdouble(0.0010)),
        cms.PSet(lowBounds=cms.vdouble(1.500,0.940),    upBounds=cms.vdouble(2.000,999.000), values=cms.vdouble(0.0118), uncertainties=cms.vdouble(0.0015)),
        cms.PSet(lowBounds=cms.vdouble(2.000,-999.000), upBounds=cms.vdouble(6.000,0.940),   values=cms.vdouble(0.0205), uncertainties=cms.vdouble(0.0010)),
        cms.PSet(lowBounds=cms.vdouble(2.000,0.940),    upBounds=cms.vdouble(6.000,999.000), values=cms.vdouble(0.0165), uncertainties=cms.vdouble(0.0008)),
        ))

from flashgg.Systematics.ecalElfTools import getRunDependentScaleBins

# photonScaleBinsData = getRunDependentScaleBins('EgammaAnalysis/ElectronTools/data/76X_16DecRereco_2015_scales.dat')
photonScaleBinsData = getRunDependentScaleBins('flashgg/Systematics/data/test_2016B_scales.dat')

photonScaleUncertBins = cms.PSet(
    variables = cms.vstring("abs(superCluster.eta)","r9"),
    bins = cms.VPSet(
        ## only uncertainties here. scales loaded by SystematicsCustomize according to process.photonScaleBinsData
            cms.PSet( lowBounds = cms.vdouble(0.000 , -999.000 ) , upBounds = cms.vdouble(1.000 , 0.940   ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00050 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(0.000 , 0.940    ) , upBounds = cms.vdouble(1.000 , 999.000 ) , values = cms.vdouble( 0.  ) , uncertainties = cms.vdouble( 0.00050 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(1.000 , -999.000 ) , upBounds = cms.vdouble(1.500 , 0.940   ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00120 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(1.000 , 0.940    ) , upBounds = cms.vdouble(1.500 , 999.000 ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00060 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(1.500 , -999.000 ) , upBounds = cms.vdouble(2.000 , 0.940   ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00200 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(1.500 , 0.940    ) , upBounds = cms.vdouble(2.000 , 999.000 ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00300 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(2.000 , -999.000 ) , upBounds = cms.vdouble(6.000 , 0.940   ) , values = cms.vdouble( 0. ) ,  uncertainties = cms.vdouble( 0.00200 )   ) ,
            cms.PSet( lowBounds = cms.vdouble(2.000 , 0.940    ) , upBounds = cms.vdouble(6.000 , 999.000 ) , values = cms.vdouble( 0.  ) , uncertainties = cms.vdouble( 0.00300 )   ) ,
                    ))
