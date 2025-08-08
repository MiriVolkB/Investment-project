public class Main {
    monthly_investment = 7000
    yearly_increase = 0.02
    yearly_appreteation = 0.08
    yearly_sum = 0
    YEARS = 20

    for(int i=1; i<YEARS; i++)
    {
        if(i==1)
                monthly_investment = monthly_investment
        else
            monthly_investment = monthly_investment * yearly_increase
        growth = monthly_investment * 12
        yearly_sum =  (growth + yearly_sum) * yearly_appreteation
    }
}
