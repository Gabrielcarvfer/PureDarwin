#!/usr/bin/env python

def load_roots(str, list):
    list = [line.strip() for line in open(str, 'r')]
    return


# Put here supported options
##Of Darwin itself
darwin_releases = {
    0: "9",  # Darwin9
    1: "10",  # Darwin10
}

darwin_buildversions = {
    9: ["9J61pd1", "9G55pd1", "9F33pd1", "9L30", "9J61", "9G55", "9F33", "9E17", "9D34", "9C31", "9B18", "9A581"],
    10: ["10C540", "10B504", "10A432"],
}

darwin_architectures = {
    0: "ppc",
    1: "i386",
    2: "x86_64"
}

darwin_optionals = {
    9: [
        "Chameleon",
        "MBR_Erase",
        "HFS_Journal",
        "Voodoo",
        "PureFoundation",
        "VMWare",
        "MacFuse",
        "Login",
        "Keymap",
        "WindowM",
        "Shell",
        "Build",
        "System",
    ],

    10: [
        "Voodoo",
        "PureFoundation",
    ]
}

# Configured as default, change if needded on the option section below
darwin_optionals_details = {
    9: {
        "Chameleon": [("RC1", False), ("RC2", False), ("RC3", False), ("RC4", True)],
        "Voodoo": [("XNU", True), ("XNU9.5", True), ("XNU9.7", False), ("XNUSpeedstep", False), ("PowerMini", False),
                   ("PS2Controller", True)],
        "VMWare": [("VMDK", True), ("IDE_DRIVE", False)],
        "MacFuse": [("Ramdisk", True), ("SSHFS", True)],
        "Login": [("DefaultUser", True)],
        "Keymap": [("Belge", False), ("Deutsch", False), ("Francais", False), ("UK", False), ("USA", True)],
        "WindowM": [("X11", True), ("Wmaker", False)],
        "Shell": [("Bash", True), ("BashRC", True), ("Zsh", False), ("Zshrc", True)],
        "Build": [("Debug", True), ("Developer", True), ("TCL", True), ("SettingsFiles", True), ("Clone", True),
                  ("ClonePackages", True), ("Dtrace", True), ("KextCache", True)],
        "System": [("Launchd", True), ("Getty", True), ("NanoShell", False), ("Installer", False),
                   ("MDNSresponder", True), ("Portmap", True), ("Statd", True)],
    },

    10: {
        "Voodoo": [],
        "PureFoundation": [],
    }

}
##Of PureDarwin
puredarwin_flavours = {
    0: "base",  # or nano
    1: "default"
}
puredarwin_flavours_roots = {
    "base": [
        "temp",  # trying to fix the complete build first, so just a placeholder
    ],

    "default": []

}

load_roots("../setup/pd_roots", puredarwin_flavours_roots["default"])

darwin_optionals_default_option = ["Chameleon", "MBR_Erase", "HFS_Journal", "Voodoo", "PureFoundation", "VMWare",
                                   "MacFuse", "Login", "Keymap", "WindowM", "Shell", "Build", "System", ]

#############################      YOU CAN PLAY HERE      ###########################################################
# Select between options
darwin_release_option = 1
darwin_arch_option = 1
darwin_build_option = 1
darwin_optionals_option = darwin_optionals_default_option

# if you want to disable an option category, remove from the list
# delete darwin_optionals_option[index];



############################      STOP PLAYING HERE        ##########################################################
# Here stuff is resolved based on previous options
temp_dir = "pd_tmp"
dest_dir = temp_dir + "/Packages_D" + darwin_releases[darwin_release_option] + "_" + darwin_architectures[
    darwin_arch_option]

binary_roots_dir = temp_dir + "/Roots"


# Fetch only necessary binary roots or update if they have been downloaded previously
# placeholder
#		git clone https://github.com/PureDarwin/puredarwin.roots.git tmp_dir
#	or
#		git fetch
#		git checkout -f #--debug

# Thin packages
# placeholder
# tar zxf rootfolder destdir_temp
# thinfile arch file
# tar cjf rootfolder -C destdir_temp .


# Load terminal and export variables that are necessary
# placeholder

# Execute setyp
# placeholder
