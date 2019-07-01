import FWCore.ParameterSet.Config as cms

# This config was generated automatically using generate2023Geometry.py
# If you notice a mistake, please update the generating script, not just this config

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring(
        'Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/v2/cmsextent.xml',
        'Geometry/CMSCommonData/data/cms/2023/v1/cms.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/caloBase/2023/v1/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/muonBase/2023/v2/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/beampipe/2023/v1/beampipe.xml',
        'Geometry/CMSCommonData/data/cmsBeam/2023/v1/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/CMSCommonData/data/cavern/2017/v2/cavern.xml',
        'Geometry/CMSCommonData/data/cavernData/2017/v1/cavernData.xml',
        'Geometry/CMSCommonData/data/cavernFloor/2017/v1/cavernFloor.xml',
        'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker613/pixfwd.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker404/pixbar.xml',
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker404/otst.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker613/tracker.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker613/pixel.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker404/trackerbar.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker404/trackerfwd.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker404/trackerStructureTopology.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker613/pixelStructureTopology.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker404/trackersens.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker404/pixelsens.xml',
        'Geometry/TrackerRecoData/data/PhaseII/TiltedTracker613/trackerRecoMaterial.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker404/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker404/pixelProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/EcalCommonData/data/eregalgo/2023/v1/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/escon/2023/v1/escon.xml',
        'Geometry/EcalCommonData/data/esalgo/2023/v1/esalgo.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/hcal/NoHE/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/hcalSimNumbering/NoHE/hcalSimNumbering.xml',
        'Geometry/HcalCommonData/data/hcalRecNumbering/NoHE/hcalRecNumbering.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/HGCalCommonData/data/hgcalMaterial/v1/hgcalMaterial.xml',
        'Geometry/HGCalCommonData/data/hgcal/v9/hgcal.xml',
        'Geometry/HGCalCommonData/data/hgcalEE/v9/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/hgcalHEsil/v9/hgcalHEsil.xml',
        'Geometry/HGCalCommonData/data/hgcalHEmix/v9/hgcalHEmix.xml',
        'Geometry/HGCalCommonData/data/hgcalwafer/v9/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/hgcalcell/v9/hgcalcell.xml',
        'Geometry/HGCalCommonData/data/hgcalCons/v9/hgcalCons.xml',
        'Geometry/MuonCommonData/data/mbCommon/2017/v2/mbCommon.xml',
        'Geometry/MuonCommonData/data/mb1/2015/v1/mb1.xml',
        'Geometry/MuonCommonData/data/mb2/2015/v1/mb2.xml',
        'Geometry/MuonCommonData/data/mb3/2015/v1/mb3.xml',
        'Geometry/MuonCommonData/data/mb4/2015/v1/mb4.xml',
        'Geometry/MuonCommonData/data/design/muonYoke.xml',
        'Geometry/MuonCommonData/data/mf/2023/v2/mf.xml',
        'Geometry/MuonCommonData/data/rpcf/2023/v1/rpcf.xml',
        'Geometry/MuonCommonData/data/gemf/TDR_BaseLine/gemf.xml',
        'Geometry/MuonCommonData/data/gem11/TDR_BaseLine/gem11.xml',
        'Geometry/MuonCommonData/data/gem21/TDR_Dev/gem21.xml',
        'Geometry/MuonCommonData/data/csc/2015/v1/csc.xml',
        'Geometry/MuonCommonData/data/mfshield/2023/v1/mfshield.xml',
        'Geometry/MuonCommonData/data/me0/TDR_Dev/me0.xml',
        'Geometry/ForwardCommonData/data/forwardshield/2017/v1/forwardshield.xml',
        'Geometry/ForwardCommonData/data/brmrotations.xml',
        'Geometry/ForwardCommonData/data/PostLS2/brm.xml',
        'Geometry/ForwardCommonData/data/zdcmaterials.xml',
        'Geometry/ForwardCommonData/data/lumimaterials.xml',
        'Geometry/ForwardCommonData/data/zdcrotations.xml',
        'Geometry/ForwardCommonData/data/lumirotations.xml',
        'Geometry/ForwardCommonData/data/zdc.xml',
        'Geometry/ForwardCommonData/data/zdclumi.xml',
        'Geometry/ForwardCommonData/data/cmszdc.xml',
        'Geometry/MTDCommonData/data/btl.xml',
        'Geometry/MTDCommonData/data/etl.xml',
        'Geometry/MTDCommonData/data/CrystalBarPhiFlat/mtd.xml',
        'Geometry/MTDCommonData/data/CrystalBarPhiFlat/mtdStructureTopology.xml',
        'Geometry/MTDCommonData/data/CrystalBarPhiFlat/mtdParameters.xml',
    )+
    cms.vstring(
        'Geometry/MuonCommonData/data/muonNumbering/TDR_DeV/muonNumbering.xml',
        'Geometry/EcalSimData/data/PhaseII/ecalsens.xml',
        'Geometry/HcalCommonData/data/hcalsens/NoHE/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/HGCalSimData/data/hgcsensv9.xml',
        'Geometry/MuonSimData/data/PhaseII/ME0EtaPart/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/2023/v1/RPCSpecs.xml',
        'Geometry/GEMGeometryBuilder/data/v7/GEMSpecsFilter.xml',
        'Geometry/GEMGeometryBuilder/data/v7/GEMSpecs.xml',
        'Geometry/ForwardCommonData/data/brmsens.xml',
        'Geometry/ForwardSimData/data/zdcsens.xml',
        'Geometry/MTDSimData/data/CrystalBarPhiFlat/mtdsens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/HGCalSimData/data/hgcProdCutsv9.xml',
        'Geometry/MuonSimData/data/PhaseII/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/zdcProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/MTDSimData/data/CrystalBarPhiFlat/mtdProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml',
    ),
    rootNodeName = cms.string('cms:OCMS')
)
