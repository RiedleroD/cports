pkgname = "gbsplay"
pkgver = "0.0.104"
pkgrel = 0
build_style = "configure"
# --without-test just disables test *at build time* - tests will still run during check()
configure_args = ["--prefix=/usr", "--mandir=/usr/share/man", "--without-test"]
make_check_target = "test"
hostmakedepends = ["bash"]
pkgdesc = "Game Boy sound player"
license = "GPL-1.0-or-later"
url = "https://github.com/mmitch/gbsplay"
source = f"{url}/releases/download/{pkgver}/gbsplay-{pkgver}.tar.gz"
sha256 = "24d377046a774dd2bfa18e36afd7382d37a27715733954150b383a6a0ea4da06"
hardening = ["vis", "cfi"] # sst fails
# TODO: xgbsplay as separate package