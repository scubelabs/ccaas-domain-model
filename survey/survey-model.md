# Survey and Voice-of-Customer Model

## Entities
SurveyDefinition → SurveyVersion → Section/Question. Invitation references customer/contact point, interaction where applicable, delivery channel, eligibility policy and expiry. Response references the exact SurveyVersion and Invitation.

Question types can include rating scale, NPS-style scale, multiple choice, free text and consent/opt-in where lawful and appropriately designed.

## Metrics
Derived metrics such as CSAT, NPS or CES retain metric-definition version, source question/scale and population.

## Bias and population
Reporting should preserve eligibility, invitations, delivery success, response rate and sampling policy. A response score without denominator/population context can misrepresent customer sentiment.

## Privacy
Free-text responses can contain sensitive information and should inherit appropriate classification, access, retention and redaction policies.
