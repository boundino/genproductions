import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(1.0),
                         crossSection = cms.untracked.double(425.6),
                         comEnergy = cms.double(5020.0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'WeakBosonAndParton:qqbar2gmZg = on',
            'WeakBosonAndParton:qg2gmZq = on',,
            '23:onMode = off',
            '23:onIfAny = 13',
            'PhaseSpace:pTHatMin = 30.',
            'PhaseSpace:bias2Selection = on',
            'PhaseSpace:bias2SelectionPow = 1.5',
            'PhaseSpace:bias2SelectionRef = 30',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

zgenfilter = cms.EDFilter("PythiaFilter",
    MaxRapidity = cms.untracked.double(2.5),
    MinRapidity = cms.untracked.double(-2.5),
    MinPt = cms.untracked.double(30.),
    ParticleID = cms.untracked.int32(23)
)

ProductionFilterSequence = cms.Sequence(generator*zgenfilter)
