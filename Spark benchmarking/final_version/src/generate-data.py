from faker import Faker


def make_file(num_rows, num_columns):
    fake = Faker()
    a = ['address', 'administrative_unit', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email',
         'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'bothify', 'bs', 'building_number',
         'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 'color_name', 'company',
         'company_email', 'company_suffix', 'country', 'country_calling_code', 'country_code', 'credit_card_expire',
         'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code',
         'cryptocurrency_code', 'cryptocurrency_name', 'currency_code', 'currency_name', 'currency_symbol',
         'current_country', 'current_country_code', 'date', 'day_of_month', 'day_of_week', 'dga', 'domain_name',
         'domain_word', 'email', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name',
         'first_name_female', 'first_name_male', 'first_name_nonbinary', 'fixed_width', 'free_email',
         'free_email_domain', 'hex_color', 'hexify', 'hostname', 'http_method', 'iana_id', 'iban', 'image_url',
         'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 'ipv4_private',
         'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'itin', 'job', 'json', 'language_code', 'language_name',
         'last_name', 'last_name_female', 'last_name_male', 'last_name_nonbinary', 'lexify', 'license_plate',
         'linux_platform_token', 'linux_processor', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5',
         'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name',
         'msisdn', 'name', 'name_female', 'name_male', 'name_nonbinary', 'nic_handle', 'numerify', 'opera', 'paragraph',
         'password', 'phone_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode',
         'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'prefix_nonbinary', 'pricetag',
         'random_element', 'random_letter', 'random_lowercase_letter', 'random_uppercase_letter', 'rgb_color',
         'rgb_css_color', 'ripe_id', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email', 'safe_hex_color',
         'secondary_address', 'sentence', 'sha1', 'sha256', 'slug', 'ssn', 'state', 'state_abbr', 'street_address',
         'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift',
         'swift11', 'swift8', 'text', 'time', 'timezone', 'tld', 'unix_device', 'unix_partition', 'upc_a', 'upc_e',
         'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4',
         'windows_platform_token', 'word', 'year', 'zipcode', 'zipcode_in_state', 'zipcode_plus4']
    counter = 1
    tmp = ''
    for i in range(num_columns):
        if len(a) * counter < i:
            counter += 1
        tmp += f'{a[i % len(a)]}{counter},'
    tmp = tmp[:-1]
    tmp += '\n'
    with open(f'rows{num_rows}_columns{num_columns}.csv', 'w') as f:
        f.write(tmp)
    for i in range(num_rows):
        tmp = ''
        for j in range(num_columns):
            o = str(getattr(fake, a[j % len(a)])()).replace("\n", " ").replace(",", "_").replace("\"", "").replace("\'",
                                                                                                                   "")
            tmp += f'{o},'
        tmp = tmp[:-1]
        tmp += '\n'
        with open(f'rows{num_rows}_columns{num_columns}.csv', 'a') as f:
            f.write(tmp)


files = [(100, 50), (1000, 50), (10000, 50)]
for num_rows, num_columns in files:
    make_file(num_rows, num_columns)
