#Embedded file name: toontown.coghq.LawbotOfficeDiamondRoom_Trap00
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone13a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 100002: {'type': 'button',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-10.796, 37.9181, 0),
          'hpr': Vec3(23.9625, 0, 0),
          'scale': Vec3(3, 3, 3),
          'color': Vec4(1, 1, 1, 1),
          'isOn': 0,
          'isOnEvent': 0,
          'secondsOn': -1.0},
 100003: {'type': 'button',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-11.023, -40.7364, 0),
          'hpr': Vec3(338.199, 0, 0),
          'scale': Vec3(3, 3, 3),
          'color': Vec4(1, 1, 1, 1),
          'isOn': 0,
          'isOnEvent': 0,
          'secondsOn': -1.0},
 100006: {'type': 'door',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 100010,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(1.02303, 0, 0),
          'scale': Vec3(1, 1, 1),
          'color': Vec4(1, 1, 1, 1),
          'isLock0Unlocked': 0,
          'isLock1Unlocked': 1,
          'isLock2Unlocked': 0,
          'isLock3Unlocked': 1,
          'isOpen': 0,
          'isOpenEvent': 0,
          'isVisBlocker': 1,
          'secondsOpen': 1,
          'unlock0Event': 100000,
          'unlock1Event': 0,
          'unlock2Event': 100001,
          'unlock3Event': 0},
 100000: {'type': 'laserField',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-57.9165, 36.4902, 0.05),
          'hpr': Vec3(296.565, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 0,
          'gridGame': 'Random',
          'gridScaleX': 40.0,
          'gridScaleY': 40.0,
          'laserFactor': 3,
          'modelPath': 0,
          'projector': Point3(21, 21, 25),
          'switchId': 100002},
 100001: {'type': 'laserField',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-40.0571, -3.38424, 0.07),
          'hpr': Vec3(243.435, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 1,
          'gridGame': 'Random',
          'gridScaleX': 37.0,
          'gridScaleY': 38.0,
          'laserFactor': 3,
          'modelPath': 0,
          'projector': Point3(21, 21, 25),
          'switchId': 100003},
 100008: {'type': 'model',
          'name': 'testMoverModel',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.6, 0.6, 0.6),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2'},
 100011: {'type': 'model',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-66.4031, -28.3337, 0),
          'hpr': Vec3(330.945, 0, 0),
          'scale': Point3(0.6, 0.6, 0.6),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_stacks'},
 100012: {'type': 'model',
          'name': 'copy of <unnamed> (2)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-61.3414, 28.3839, 0),
          'hpr': Vec3(330.945, 0, 0),
          'scale': Point3(0.6, 0.6, 0.6),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_stacks'},
 100013: {'type': 'model',
          'name': 'copy of <unnamed> (3)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-73.0019, 23.1112, 0),
          'hpr': Vec3(311.424, 0, 0),
          'scale': Point3(0.6, 0.6, 0.6),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_stacks'},
 100014: {'type': 'model',
          'name': 'critbox4',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-10.5395, 55.5366, 0),
          'hpr': Vec3(26.5651, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100015: {'type': 'model',
          'name': 'critbox3',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-2.51556, -64.2189, 0),
          'hpr': Vec3(333.435, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100016: {'type': 'model',
          'name': 'critbox2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-0.559084, -27.465, 0.05),
          'hpr': Vec3(333.435, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2'},
 100019: {'type': 'model',
          'name': 'copy of crit box',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(3.82422, 21.9664, 0),
          'hpr': Vec3(60.9454, 0, 0),
          'scale': Point3(0.55, 0.55, 0.9),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100021: {'type': 'model',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 100017,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.8, 0.8, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2'},
 100022: {'type': 'model',
          'name': 'copy of <unnamed>',
          'comment': '',
          'parentEntId': 100017,
          'pos': Point3(-1.72022, 8.94383, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.8, 0.8, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2'},
 100023: {'type': 'model',
          'name': 'copy of <unnamed> (2)',
          'comment': '',
          'parentEntId': 100017,
          'pos': Point3(-1.27251, -8.84256, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.8, 0.8, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2'},
 100026: {'type': 'model',
          'name': 'crit box',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(1.3729, 25.0434, 0),
          'hpr': Vec3(26.5651, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100028: {'type': 'model',
          'name': 'copy of <unnamed> (3)',
          'comment': '',
          'parentEntId': 100027,
          'pos': Point3(-0.758049, -10.1966, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100029: {'type': 'model',
          'name': 'copy of <unnamed> (4)',
          'comment': '',
          'parentEntId': 100027,
          'pos': Point3(1.82438, -2.94686, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100030: {'type': 'model',
          'name': 'copy of <unnamed> (5)',
          'comment': '',
          'parentEntId': 100027,
          'pos': Point3(0.164113, 4.44244, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100031: {'type': 'model',
          'name': 'copy of <unnamed> (6)',
          'comment': '',
          'parentEntId': 100027,
          'pos': Point3(5.13217, 10.0594, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(0.6, 0.6, 0.8),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100035: {'type': 'model',
          'name': 'copy of crit box (2)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(3.01721, -23.3741, 0),
          'hpr': Vec3(13.2405, 0, 0),
          'scale': Point3(0.55, 0.55, 0.9),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100036: {'type': 'model',
          'name': 'copy of crit box (2)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-8.58923, 61.9548, 0),
          'hpr': Vec3(26.5651, 0, 0),
          'scale': Point3(0.55, 0.55, 0.9),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3'},
 100018: {'type': 'mover',
          'name': 'testMover',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-64.3817, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cycleType': 'return',
          'entity2Move': 100008,
          'modelPath': 0,
          'moveTarget': 100034,
          'pos0Move': 2,
          'pos0Wait': 2,
          'pos1Move': 2,
          'pos1Wait': 2,
          'startOn': 0,
          'switchId': 0},
 100024: {'type': 'mover',
          'name': 'paperwall2mover',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, -46.3957, 0),
          'hpr': Vec3(333.435, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cycleType': 'oneWay',
          'entity2Move': 100017,
          'modelPath': 0,
          'moveTarget': 100025,
          'pos0Move': 2,
          'pos0Wait': 2,
          'pos1Move': 2,
          'pos1Wait': 2,
          'startOn': 0,
          'switchId': 100001},
 100032: {'type': 'mover',
          'name': 'paperwall1mover',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-1.54332, 42.0157, 0),
          'hpr': Vec3(26.5651, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cycleType': 'oneWay',
          'entity2Move': 100027,
          'modelPath': 0,
          'moveTarget': 100033,
          'pos0Move': 2,
          'pos0Wait': 2,
          'pos1Move': 2,
          'pos1Wait': 2,
          'startOn': 0,
          'switchId': 100000},
 100004: {'type': 'nodepath',
          'name': 'BattlePos1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-31.9689, 28.7456, 0),
          'hpr': Vec3(22.6199, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100005: {'type': 'nodepath',
          'name': 'BattlePos2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-31.0858, -34.9835, 0),
          'hpr': Vec3(331.39, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100007: {'type': 'nodepath',
          'name': 'copy of Cog Parent1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-11.0871, 37.4001, 0),
          'hpr': Vec3(299.249, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100009: {'type': 'nodepath',
          'name': 'Cog Parent1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-10.2246, -41.5943, 0),
          'hpr': Vec3(246.214, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100010: {'type': 'nodepath',
          'name': 'doorparent',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(133.9, -1.81291, 0),
          'hpr': Vec3(265.74, 0, 0),
          'scale': Point3(1, 1, 1)},
 100017: {'type': 'nodepath',
          'name': 'PaperDoor2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100020: {'type': 'nodepath',
          'name': 'movertarget',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-84.0273, -14.7227, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100025: {'type': 'nodepath',
          'name': 'papperwall2target',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(14.2998, -46.0911, 0),
          'hpr': Vec3(336.038, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100027: {'type': 'nodepath',
          'name': 'PaperWall1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100033: {'type': 'nodepath',
          'name': 'paperwall1movertarget',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(13.6684, 42.7864, 0),
          'hpr': Vec3(41.1859, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100034: {'type': 'nodepath',
          'name': 'test mover target',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-51.1549, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
