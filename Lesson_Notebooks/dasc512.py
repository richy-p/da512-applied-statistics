def linearity_test(model, y):
    '''
    Function for visually inspecting the assumption of linearity in a linear regression model.
    It plots observed vs. predicted values and residuals vs. predicted values.
    It uses Locally Weighted Scatterplot Smoothing (LOWESS) to fit a model. 
    
    Args:
    * model - fitted OLS model from statsmodels
    * y - observed values
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    pred = model.fittedvalues
    influence = model.get_influence()
    resid_std = influence.resid_studentized_internal
    
    fig, ax = plt.subplots(1,2, figsize=(7.5,3.5))
    
    sns.regplot(x=pred, y=y, lowess=True, ax=ax[0], line_kws={'color':'darkorchid'})
    # I've added the ideal line (y=yhat) for comparison
    sns.lineplot(x=[min(pred), max(pred)], y=[min(pred), max(pred)], 
                 ax=ax[0], color='red', ls=':')
    ax[0].set_title('Observed vs. Fitted Values')
    ax[0].set_xlabel('Fitted')
    ax[0].set_ylabel('Observed')
    
    sns.regplot(x=pred, y=resid_std, lowess=True, ax=ax[1], line_kws={'color':'darkorchid'})
    # I've added the ideal line (y=0) for comparison
    sns.lineplot(x=[min(pred), max(pred)], y=[0,0], ax=ax[1], color='red', ls=':')
    ax[1].set_title('Residuals vs. Fitted Values')
    ax[1].set_xlabel('Fitted')
    ax[1].set_ylabel('Standardized Residual')
    
    return fig, ax
    
def homoscedasticity_test(model):
    '''
    Function for testing the homoscedasticity of residuals in a linear regression model.
    It plots residuals and standardized residuals vs. fitted values and runs Breusch-Pagan 
    and Goldfeld-Quandt tests.
    
    Args:
    * model - fitted OLS model from statsmodels
    '''
    import statsmodels.stats.api as sms
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    
    pred = model.fittedvalues
    resid = model.resid
    resid_z = model.get_influence().resid_studentized_internal

    fig, ax = plt.subplots(1,2, figsize=(7.5,3.5))

    sns.regplot(x=pred, y=resid, lowess=True, ax=ax[0], line_kws={'color': 'darkorchid'})
    # I've added the ideal line (y=0) for comparison
    sns.lineplot(x=[min(pred), max(pred)], y=[0,0], ax=ax[0], color='red', ls=':')
    ax[0].set_title('Residuals vs. Fitted Values')
    ax[0].set(xlabel='Fitted', ylabel='Residual')

    sns.regplot(x=pred, y=np.sqrt(np.abs(resid_z)), lowess=True, ax=ax[1], line_kws={'color': 'darkorchid'})
    # I've added the ideal line for comparison
    sns.lineplot(x=[min(pred), max(pred)], y=[0.822,0.822], ax=ax[1], color='red', ls=':')
    ax[1].set_title('Scale-Location')
    ax[1].set(xlabel='Fitted', ylabel=r'$\sqrt{|{\mathrm{Standardized~Residual}}|}$')

    # Breusch-Pagan tests if regression on 'Residuals ~ Fitted Values' has non-zero slope
    # Good for picking up trends of strictly increasing or decreasing variance
    bp_test = pd.DataFrame(sms.het_breuschpagan(resid, model.model.exog), 
                           columns=['value'],
                           index=['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value'])

    # Goldfeld-Quandt tests if variance on left half of residual plot is equal to variance on right half
    gq_test = pd.DataFrame(sms.het_goldfeldquandt(resid, model.model.exog)[:-1],
                           columns=['value'],
                           index=['F statistic', 'p-value'])

    print('\n Breusch-Pagan test ----')
    print(bp_test)
    print('\n Goldfeld-Quandt test ----')
    print(gq_test)
    print('\n Residuals plots ----')
    
    fig.tight_layout()
    return fig, ax

def normality_of_residuals_test(model):
    '''
    Function for drawing the normal QQ-plot of the residuals and running 5 statistical tests to 
    investigate the normality of residuals.
    
    Arg:
    * model - fitted OLS models from statsmodels
    '''
    import scipy.stats as stats
    import statsmodels.graphics.api as smg
    import statsmodels.stats.api as sms
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(4,3.5))
    smg.qqplot(data=model.resid, line='45', fit=True, ax=ax);
    ax.set_title('Q-Q plot');
    resid_z = model.get_influence().resid_studentized_internal

    sw = stats.shapiro(model.resid)
    dp = stats.normaltest(model.resid)
    jb = stats.jarque_bera(model.resid)
    ad = stats.anderson(model.resid, dist='norm')
    lf = sms.lilliefors(model.resid)
    ks = stats.kstest(resid_z, 'norm')
    
    print(f'Shapiro-Wilk test ---- statistic: {sw[0]:.4f}, p-value: {sw[1]:.4f}')
    print(f"D'Agostino-Pearson Omnibus test ---- statistic: {dp[0]:.4f}, p-value: {dp[1]:.4f}")
    print(f'Lilliefors test ---- statistic: {lf[0]:.4f}, p-value: {lf[1]:.4f}')
    print(f'Jarque-Bera test ---- statistic: {jb[0]:.4f}, p-value: {jb[1]}')
    print(f'Kolmogorov-Smirnov test ---- statistic: {ks.statistic:.4f}, p-value: {ks.pvalue:.4f}')
    print(f'Anderson-Darling test ---- statistic: {ad.statistic:.4f}, 5% critical value: {ad.critical_values[2]:.4f}')
    print('If the returned AD statistic is larger than the critical value, then for the 5% significance level, '\
          'the null hypothesis that the data come from the Normal distribution should be rejected. ')
    
    return fig, ax

def autocorrelation_plot(model):
    import statsmodels.tsa.api as smt
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(12,6))
    acf = smt.graphics.plot_acf(model.resid, lags=40, alpha=0.05, ax=ax)
    
    return fig, ax