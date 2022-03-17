t5_requirements = {
    40: {'t7_id': 44, 'desc': 'On Hit'},
    41: {'t7_id': 47, 'desc': 'On Block'},
    48: {'t7_id': 66, 'desc': 'Opponent Standing'},
    49: {'t7_id': 67, 'desc': 'Opponent Crouching'},
    55: {'t7_id': 72, 'desc': 'Back Turned'},
    56: {'t7_id': 73, 'desc': 'Not Back Turned'},
    67: {'t7_id': 84, 'desc': '???'},
    68: {'t7_id': 85, 'desc': '???'},
    69: {'t7_id': 86, 'desc': '???'},
    70: {'t7_id': 87, 'desc': '???'},
    99: {'t7_id': 126, 'desc': 'Opponent is Downed'},
    100: {'t7_id': 127, 'desc': 'Opponent on their feet'},
    108: {'t7_id': 135, 'desc': 'Death'},
    111: {'t7_id': 146, 'desc': 'Standing on left side'},
    112: {'t7_id': 147, 'desc': 'Standing on right side'},
    113: {'t7_id': 148, 'desc': 'On ground (right side)'},
    114: {'t7_id': 149, 'desc': 'On ground (left side)'},
    133: {'t7_id': 182, 'desc': 'Near Wall'},
    140: {'t7_id': 216, 'desc': 'Wall splat related'},
    184: {'t7_id': 352, 'desc': 'Check value (prop 0x80a6)'},
    321: {'t7_id': 881, 'desc': 'Requirements end'},
}

t5_extra_move_properties = {
    0x8001: {'t7_id': 0x8001, 'desc': 'Minimum Camera Shake'},
    0x8002: {'t7_id': 0x8003, 'desc': 'Heavy Camera Shake'},
    0x8003: {'t7_id': 0x8004, 'desc': 'Heaviest Camera Shake'},
    0x8004: {'t7_id': 0x8006, 'desc': 'Minimum Camera Shake'},
    0x8006: {'t7_id': 0x8008, 'desc': 'Heavy Camera Shake'},
    0x8007: {'t7_id': 0x8009, 'desc': 'Heaviest Camera Shake'},
    0x8019: {'t7_id': 0x802E, 'desc': 'Play Player Hit Spark on Self'},
    0x804B: {'t7_id': 0x80A6, 'desc': 'Value Store (req 352)'},
    0x8067: {'t7_id': 0x817D, 'desc': 'Give CH property'},
    0x8073: {'t7_id': 0x818C, 'desc': '(Tco_dwupR50) Kazuya'},
    0x8076: {'t7_id': 0x818D, 'desc': '(HEIHACHI-SideEscL_n) SideEscL_n'},
    0x8077: {'t7_id': 0x818E, 'desc': '(HEIHACHI-wDm_AirF_Up) wDm_AirF_Up'},
    0x8078: {'t7_id': 0x8193, 'desc': '(HEIHACHI-He_sDASHF) He_sDASHF'},
    0x807D: {'t7_id': 0x8198, 'desc': '(HEIHACHI-He_sDASHB) He_sDASHB'},
    0x807F: {'t7_id': 0x8199, 'desc': '(dwup_hei_xe) Kazuya'},
    0x8081: {'t7_id': 0x81A3, 'desc': '(Tco_dwupR50) Kazuya'},
    0x8082: {'t7_id': 0x81A4, 'desc': '(dwup_hei_xU) Kazuya'},
    0x80E3: {'t7_id': 0x853D, 'desc': '(sDw_AIR00_) Kazuya'},
    0x80E4: {'t7_id': 0x824C, 'desc': '(sDw_AIR00_) Kazuya'},
    0x813E: {'t7_id': 0x8428, 'desc': 'Both Hands Pose'},
    0x813F: {'t7_id': 0x8429, 'desc': 'Left Hand Pose'},
    0x8140: {'t7_id': 0x842A, 'desc': 'Right Hand Pose'},
    0x8141: {'t7_id': 0x842C, 'desc': 'Right Hand MOT related'},
    0x8142: {'t7_id': 0x842D, 'desc': 'Both Hands Animation'},
    # Parameters start from 0x4000. Same as in T7
    0x8143: {'t7_id': 0x842E, 'desc': 'Left Hand Animation'},
    # Parameters start from 0x4000. Same as in T7
    0x8144: {'t7_id': 0x842F, 'desc': 'Right Hand Animation'},
    # Parameters start from 0x4000. Same as in T7
    0x8147: {'t7_id': 0x8435, 'desc': 'Cinematic Camera'},
    0x814C: {'t7_id': 0x84C2, 'desc': 'Play Facial Animation'},
    0x814E: {'t7_id': 0x84C4, 'desc': 'Play Player Sound'},
    0x814F: {'t7_id': 0x84C6, 'desc': 'Play Opponent Sound'},
    # Parameter format same for voicelines, except they are in 2 bytes.
    # For T7: 0x0F000000
    # For T5: 0x0F00    
    0x8152: {'t7_id': 0x84CB, 'desc': 'Play Attached Audio'},
    0x8153: {'t7_id': 0x84CC, 'desc': 'Preset Camera Zoom'},
}
