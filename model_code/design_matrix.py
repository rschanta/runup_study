def design_matrix_base():
      return {
          
      "Title": {
            "TITLE": "DYNAMIC"
      },

      "Parallel Info": {
            "PX": "24",
            "PY": "1"
      },

      "Depth": {
            "DEPTH_TYPE": "DATA",
      },

      "Dimension": {
            "Mglob": "DYNAMIC",
            "Nglob": "3"
      },

      "Time": {
            "TOTAL_TIME": "DYNAMIC",
            "PLOT_INTV": "0.2",
            "PLOT_INTV_STATION": "0.1",
            "SCREEN_INTV": "25.0"
      },

      "Grid": {
            "DX": "DYNAMIC",
            "DY": "DYNAMIC"
      },

      "Wavemaker": {
            "WAVEMAKER": "WK_REG",
            "Xc_WK": "DYNAMIC",
            "DEP_WK": "DYNAMIC",
            "Yc_WK": "0.0",
            "Theta_WK": "0.0",
            "Delta_WK": "3.0"
      },

      "Periodic Boundary Condition": {
            "PERIODIC": "F"
      },

      "Sponge Layer": {
            "DIFFUSION_SPONGE": "F",
            "FRICTION_SPONGE": "T",
            "DIRECT_SPONGE": "T",
            "Sponge_south_width": "0.0",
            "Sponge_north_width": "0.0",
            "Sponge_west_width": "DYNAMIC",
            "Sponge_east_width": "0.0"
      },

      "Friction": {
            "Cd": "0.00",
            'FRICTION_FILE': 'DYNAMIC',
            'FRICTION_MATRIX': 'T'
      },

      "Numerics": {
            "CFL": "0.4",
            "FroudeCap": "3.0",
      },

      "Wet-Dry": {
            "MinDepth": "0.01",
            "VISCOSITY_BREAKING": "T"
      },

      "Breaking": {
            "Cbrk1": "0.65",
            "Cbrk2": "0.35",
            "SHOW_BREAKING": "T",
            "ROLLER_EFFECT": "T",
      },


      "Output": {
            "FIELD_IO_TYPE": "BINARY",
            "DEPTH_OUT": "T",
            "ETA": "T",
            "MASK": "T",
            "AGE": "F",
            "UNDERTOW": "F",
            "OUT_NU": "F",
            "U": "F",
            "V": "F",
            'STATION_FILE': 'DYNAMIC'
      },


      }
