package main.java.design;

import java.util.List;

class PackageService implements PackageServiceI {

    @Override
    public boolean isPackageSize(int size) {
        return false;
    }

    @Override
    public boolean isDependent(String name) {
        return false;
    }

    @Override
    public boolean isLicenseBlocked(List<String> blockedLicenses) {
        return false;
    }
}
