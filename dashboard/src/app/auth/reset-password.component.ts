import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
    selector: 'app-reset-password',
    standalone: true,
    imports: [CommonModule, FormsModule],
    template: `
    <div class="auth-wrapper">
      <div class="glass-panel auth-card">
        <h1>New Password</h1>
        <p class="subtitle">Secure your account with a new password</p>
        
        <form (submit)="onSubmit($event)">
          <input type="password" name="password" [(ngModel)]="password" placeholder="New Password" required>
          <input type="password" name="confirm" [(ngModel)]="confirmPassword" placeholder="Confirm Password" required>
          <button type="submit" class="btn-primary w-full" [disabled]="loading">
            {{ loading ? 'UPDATING...' : 'UPDATE PASSWORD' }}
          </button>
        </form>

        <div *ngIf="message" class="success-msg">{{ message }}</div>
      </div>
    </div>
  `,
    styles: [`
    .success-msg { color: #00f2ff; margin-top: 1rem; font-size: 0.9rem; }
  `]
})
export class ResetPasswordComponent {
    private authService = inject(AuthService);
    private router = inject(Router);
    private route = inject(ActivatedRoute);

    password = '';
    confirmPassword = '';
    loading = false;
    message = '';

    onSubmit(e: Event) {
        e.preventDefault();
        if (this.password !== this.confirmPassword) {
            alert("Passwords do not match");
            return;
        }

        const token = this.route.snapshot.queryParams['token'];
        this.loading = true;
        this.authService.confirmPasswordReset({ token, new_password: this.password }).subscribe({
            next: (res) => {
                this.message = res.message;
                this.loading = false;
                setTimeout(() => this.router.navigate(['/login']), 2000);
            },
            error: () => this.loading = false
        });
    }
}
