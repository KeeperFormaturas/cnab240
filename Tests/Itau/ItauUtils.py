from keeper_cnab240.company import Company

company = Company('BF Servicos De Cobranca Ltda', '07179434000140')
company.set_bank_acccount(341, '0772', '69637', 3)
company.set_address('Av. Andrômeda', 2000, 'Bl.8-4 andar', 'Alphaville Residencial Plus', 'Barueri', 'SP', '06473000')

company_j = Company('Arizona 701', '20093235000182')
company_j.set_bank_acccount(237, '0296', '1081', 2)
company_j.set_address('Rua Arizona', 701, '', 'Brooklin', 'São Paulo', 'SP', '04567002')
