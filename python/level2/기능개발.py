COMPLETE_VALUE = 100


def solution(progresses, speeds):
    answer = []

    # 복사 후 사용
    jobs = progresses
    speed = speeds

    completed_jobs = []

    while len(completed_jobs) != len(jobs):
        do_work(jobs, speed)

        while True:
            if len(jobs) > 0 and jobs[0] >= COMPLETE_VALUE:
                completed_jobs.append(jobs.pop(0))
                speed.pop(0)
            else:
                break

        completed_jobs_size = len(completed_jobs)

        if completed_jobs_size > 0:
            answer.append(completed_jobs_size)

        completed_jobs.clear()

    return answer


def do_work(jobs, speed):
    for i in range(0, len(jobs)):
        jobs[i] += speed[i]