package main.java.design;

import java.util.List;

interface PackageServiceI {
    boolean isPackageSize(int size);
    boolean isDependent (String name);
    boolean isLicenseBlocked(List<String> blockedLicenses);

}
