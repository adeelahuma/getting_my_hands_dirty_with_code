package main.java.design;

import java.util.ArrayList;
import java.util.List;

public class Package {
    private String name;
    private String version;
    private int size;
    private String license;
    private List<Package> dependentPackages ;

    public String getName() {
        return name;
    }

    public String getVersion() {
        return version;
    }

    public int getSize() {
        return size;
    }

    public String getLicense() {
        return license;
    }

    public List<Package> getDependentPackages() {
        return dependentPackages;
    }

    public Package getPackage(String name, String version){
        return new Package();
    }

    public int getInstalledSize(){

        int installedSize = this.size;

        for (Package p : dependentPackages){
            installedSize += p.getInstalledSize();
        }

        return installedSize;
    }

    //names of dependent packages
    public List<String> getDependencies(){

        List<String> dependentLib = new ArrayList<>();

        for (Package p : dependentPackages){
            dependentLib.add(p.getName());
        }

        return dependentLib;
    }


    public List<String> getLicenses(){

        List<String> dependentLicense = new ArrayList<>();

        for (Package p : dependentPackages){
            dependentLicense.add(p.getLicense());
        }

        return dependentLicense;

    }

}


