public class PracticeBean {
    private String beanName;
    private Integer beanCount;
    private boolean active;
    int myDefaultVariable;

    public String getBeanName(){
        return beanName;
    }

    public void setBeanName(String name){
        beanName = name;
    }

    public void setActive(boolean state){
        active = state;
    }

    public boolean getActive(){   // OR isActive()
        return active;
    }

}
