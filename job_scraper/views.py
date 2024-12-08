from django.shortcuts import render
from django.http import JsonResponse
from .job_scraper_utils import configure_webdriver, search_jobs, scrape_job_data, clean_data

def scrape_jobs(request):
    if request.method == "GET":
        job_position = request.GET.get('job_position', 'web developer')
        job_location = request.GET.get('job_location', 'remote')
        country = request.GET.get('country', 'https://www.indeed.com')
        date_posted = request.GET.get('date_posted', 20)

        try:
            driver = configure_webdriver()
            full_url, total_jobs = search_jobs(driver, country, job_position, job_location, date_posted)
            df = scrape_job_data(driver, country)

            if df.empty:
                return JsonResponse({'message': 'No results found for the given criteria.', 'url': full_url})

            cleaned_df = clean_data(df)
            return JsonResponse({'message': 'Job scraping completed successfully!', 'data': cleaned_df.to_dict(), 'total_jobs': total_jobs})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        finally:
            driver.quit()

def job_scraper_home(request):
    return render(request, 'job_scraper/home.html')
